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

@app.route("/clients", methods=['POST'])
def postRequest():
   statusCode = 200
   message = ''
   try:
      requestData = request.get_json()

      if (clientDB.clientExists(requestData['companyName'])):
         raise Exception(f"Client with name {requestData['companyName']} already exists!")
         
      client = Client(requestData['companyName'], requestData['phoneNumber'], requestData['address'], requestData['registrationDate'], requestData['invoicing'])
      bankAccounts = []
      for bankAccount in requestData['bankAccounts']:
         bankAccounts.append(BankAccount(requestData['companyName'], bankAccount['codeBank'], bankAccount['agencyNumber'], bankAccount['accountNumber']))
      
      message = client.serialize()
      clientDB.insert(client)
      bankAccountsJson = []
      for bankAccount in bankAccounts:
         bankAccountsJson.append(bankAccount.serialize())
         bankAccountDB.insert(bankAccount)
      message += json.dumps({
         "bankAccounts": bankAccountsJson
      })
   except Exception as e:
      statusCode = 400
      message = e.__str__()

   return jsonify({
      'status_code': statusCode,
      'message': message,
   })

if __name__ == '__main__':
    app.run()