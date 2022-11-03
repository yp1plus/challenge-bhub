import json
from flask import Flask, request, jsonify
from database.bankAccount_db import BankAccountDatabase
from database.client_db import ClientDatabase
from models.client import Client
from models.bankAccount import BankAccount

app = Flask(__name__)

clientDB = ClientDatabase()
clientDB.createTable()
bankAccountDB = BankAccountDatabase()
bankAccountDB.createTable()

@app.route("/")
def index():
    return "Welcome to BHUB API"

@app.route('/clients', methods=['POST'])
def postRequest():
   statusCode = 200
   body = ''
   try:
      requestData = request.get_json()

      if (clientDB.clientExists(requestData['companyName'])):
         raise Exception(f"Client with name {requestData['companyName']} already exists!")
         
      client = Client(requestData['companyName'], requestData['phoneNumber'], requestData['address'], requestData['registrationDate'], requestData['invoicing'])
      bankAccounts = []
      for bankAccount in requestData['bankAccounts']:
         bankAccounts.append(BankAccount(requestData['companyName'], bankAccount['codeBank'], bankAccount['agencyNumber'], bankAccount['accountNumber']))
      
      clientJson = client.serialize()
      clientDB.insert(client)
      bankAccountsJson = []
      for bankAccount in bankAccounts:
         bankAccountsJson.append(bankAccount.serialize())
         bankAccountDB.insert(bankAccount)
      clientJson['bankAccounts'] = bankAccountsJson
      body = clientJson
   except Exception as e:
      statusCode = 400
      body = e.__str__()

   return jsonify(body), statusCode

@app.route('/clients', methods=['GET'])
def getClients():
   statusCode = 200
   body = ''
   try:
      clients = []
      for client in clientDB.viewTable():
         clientJson = client.serialize()
         clientJson['bankAccounts'] = bankAccountDB.getBankAccounts(clientJson['companyName'])
         clients.append(clientJson)
      body = clients
   except Exception as e:
      body = e.__str__()
      statusCode = 400
   return jsonify(body), statusCode

@app.route('/clients/<companyName>', methods=['GET'])
def getClient(companyName):
   statusCode = 200
   body = ''
   try:
      client = clientDB.getClient(companyName)
      clientJson = client.serialize()
      clientJson['bankAccounts'] = bankAccountDB.getBankAccounts(clientJson['companyName'])
      body = clientJson
   except Exception as e:
      body = e.__str__()
      statusCode = 400
   return jsonify(body), statusCode

if __name__ == '__main__':
    app.run()