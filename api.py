import os
from database.bankAccount_db import BankAccountDatabase
from database.client_db import ClientDatabase
from models.client import Client
from models.bankAccount import BankAccount

class API:
    def __init__(self):
        self.clientDB = ClientDatabase()
        self.bankAccountDB = BankAccountDatabase()
    
    def index():
        return "Welcome to BHUB API"
        
    def insertClient(self, requestData):
        if (self.clientDB.clientExists(requestData['companyName'])):
            raise Exception(f"Client with name {requestData['companyName']} already exists!")
                
        try:
            client = Client(requestData['companyName'], requestData['phoneNumber'], requestData['address'], requestData['registrationDate'], requestData['invoicing'])
            clientJson = client.serialize()
            bankAccountsJson = [self.__createBankAccount(requestData['companyName'], bankAccountRequest) for bankAccountRequest in requestData['bankAccounts']]
            clientJson['bankAccounts'] = bankAccountsJson
            self.clientDB.insert(client)
        except Exception as e:
            self.clientDB.delete(requestData['companyName'])
            self.bankAccountDB.deleteAllFromClient(requestData['companyName'])
            raise e
        
        return clientJson
    
    def insertBankAccount(self, companyName, requestData):
        if (self.clientDB.clientExists(companyName)):
            return self.__createBankAccount(companyName, requestData)
        else:
            raise Exception(f"The client {companyName} doesn't exist")
    
    def __createBankAccount(self, companyName, bankAccountRequest):
        bankAccount = BankAccount(None, companyName, bankAccountRequest['codeBank'], bankAccountRequest['agencyNumber'], bankAccountRequest['accountNumber'])
        self.bankAccountDB.insert(bankAccount)
        return bankAccount.serialize()
    
    def getClients(self):
        return [self.__getClientJson(client) for client in self.clientDB.viewTable()]
    
    def getClient(self, companyName):
        client = self.clientDB.getClient(companyName)
        return self.__getClientJson(client)

    def updateClient(self, companyName, req_data):
        if (not req_data):
            raise Exception("Request is empty")
        client = self.clientDB.getClient(companyName)
        if 'phoneNumber' in req_data:
            client.setPhoneNumber(req_data['phoneNumber'])
        if 'address' in req_data:
            client.setAddress(req_data['address'])
        if 'invoicing' in req_data:
            client.setInvoicing(req_data['invoicing'])
        self.clientDB.update(client)
        
        return self.__getClientJson(client)
    
    def __getClientJson(self, client):
        clientJson = client.serialize()
        clientJson['bankAccounts'] = self.bankAccountDB.getBankAccounts(clientJson['companyName'])
        return clientJson
    
    def deleteClient(self, companyName):
        self.clientDB.delete(companyName)
        self.bankAccountDB.deleteAllFromClient(companyName)

    def deleteBankAccount(self, id):
        self.bankAccountDB.delete(id)
    
    def getBankAccount(self, id):
        bankAccount = self.bankAccountDB.getBankAccount(id)
        return bankAccount.serialize()
    
    def getBankAccounts(self, companyName):
        return self.bankAccountDB.getBankAccounts(companyName)