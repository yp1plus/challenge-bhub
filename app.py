from flask import Flask, request, jsonify
from api import API

app = Flask(__name__)

api = API()

@app.route("/")
def initialize():
   return api.index()

@app.route('/clients', methods=['POST', 'GET'])
def controlClients():
   statusCode = 200
   body = ''
   try:
      if (request.method == 'POST'):
         requestData = request.get_json()
         body = api.insertClient(requestData)
      elif (request.method == 'GET'):
         body = api.getClients()
   except Exception as e:
      statusCode = 400
      body = e.__str__()

   return jsonify(body), statusCode

@app.route('/clients/<companyName>', methods=['GET', 'PUT', 'DELETE'])
def controlClient(companyName):
   statusCode = 200
   body = ''
   try:
      if (request.method == 'GET'):
         body = api.getClient(companyName)
      elif (request.method == 'PUT'):
         requestData = request.get_json()
         body = api.updateClient(companyName, requestData)
      elif (request.method == 'DELETE'):
         api.deleteClient(companyName)
         body  = 'Deleted with success'
   except Exception as e:
      statusCode = 400
      body = e.__str__()
   return jsonify(body), statusCode

@app.route('/clients/<companyName>/bankAccounts', methods=['GET', 'POST'])
def controlBankAccounts(companyName):
   statusCode = 200
   body = ''
   try:
      if (request.method == 'GET'):
         body = api.getBankAccounts(companyName)
      elif (request.method == 'POST'):
         requestData = request.get_json()
         body = api.insertBankAccount(companyName, requestData)
   except Exception as e:
      statusCode = 400
      body = e.__str__()

   return jsonify(body), statusCode

@app.route('/clients/bankAccounts/<id>', methods=['GET', 'DELETE'])
def controlBankAccount(id):
   statusCode = 200
   body = ''
   try:
      if (request.method == 'GET'):
         body = api.getBankAccount(id)
      elif (request.method == 'DELETE'):
         api.deleteBankAccount(id)
         body = 'Deleted with success'
   except Exception as e:
      statusCode = 400
      body = e.__str__()
   return jsonify(body), statusCode

if __name__ == '__main__':
    app.run()