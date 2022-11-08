import json
from models.bankAccount import BankAccount
from database.db import Database
from database.client_db import ClientDatabase

class BankAccountDatabase:
    def __init__(self):
        self.NAME = 'bankAccounts'
        self.database = Database(self.NAME)
        self.createTable()
    
    def createTable(self):
        self.database.executeFunction(f"CREATE TABLE IF NOT EXISTS {self.NAME} (id TEXT PRIMARY KEY, companyName TEXT NOT NULL, codeBank TEXT, agencyNumber TEXT, accountNumber TEXT)")

    def populateTable(self):
        with open('data/bankAccounts.json', 'r') as bankAccounts:
            data = json.load(bankAccounts)
        
        for bankAccount in data:
            self.insert(BankAccount(bankAccount['companyName'], bankAccount['codeBank'], bankAccount['agencyNumber'], bankAccount['accountNumber']))

    def insert(self, bankAccount):
        self.database.insert(bankAccount)
    
    def viewTable(self):
        rows = self.database.getRows()
        bankAccounts = []
        for row in rows:
            bankAccount = BankAccount(row[0], row[1], row[2], row[3], row[4])
            bankAccounts.append(bankAccount)
        return bankAccounts
    
    def getBankAccounts(self, companyName):
        bankAccounts = [bankAccount.serialize() for bankAccount in self.viewTable()]
        def checkCompanyName(bankAccount):
            return bankAccount['companyName'] == companyName
        bankAccountsFromClient = list(filter(checkCompanyName, bankAccounts))

        return bankAccountsFromClient
    
    def getBankAccount(self, id):
        row = self.database.getRow({'id': id})
        bankAccount = BankAccount(row[0], row[1], row[2], row[3], row[4])
        return bankAccount

    def delete(self, id):
        self.database.delete({'id': id})
    
    def deleteAllFromClient(self, companyName):
        bankAccounts = self.getBankAccounts(companyName)
        for bankAccount in bankAccounts:
            self.delete(bankAccount['id'])

    def deleteAll(self):
        self.database.deleteAll()

