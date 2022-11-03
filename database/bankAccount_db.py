import json
from models.bankAccount import BankAccount
from database.db import Database

class BankAccountDatabase:
    def __init__(self):
        self.NAME = 'bankAccounts'
        self.database = Database(self.NAME)
    
    def createTable(self):
        self.database.executeFunction(f"CREATE TABLE IF NOT EXISTS {self.NAME} (id TEXT PRIMARY KEY, companyName TEXT NOT NULL, codeBank TEXT, agencyNumber TEXT, accountNumber TEXT, FOREIGN KEY(companyName) REFERENCES clients (companyName))")

    def populateTable(self):
        with open('database/bankAccounts.json', 'r') as bankAccounts:
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

    def update(self, bankAccount):
        properties = {
            'agencyNumber': bankAccount.agencyNumber,
            'accountNumber': bankAccount.accountNumber
        }
        key = {
            'id': bankAccount.id
        }
        self.database.update(properties, key)

    def delete(self, id):
        self.database.delete({'id': id})

    def deleteAll(self):
        self.database.deleteAll()

