import json
from models.client import Client
from database.db import Database

class ClientDatabase:
    def __init__(self):
        self.NAME = 'clients'
        self.database = Database(self.NAME)
    
    def createTable(self):
        self.database.executeFunction(f"CREATE TABLE IF NOT EXISTS {self.NAME} (companyName TEXT PRIMARY KEY, phoneNumber TEXT, address TEXT, registrationDate TEXT, invoicing REAL)")

    def populateTable(self):
        with open('database/clients.json', 'r') as clients:
            data = json.load(clients)
        
        for client in data:
            self.insert(Client(client['companyName'], client['phoneNumber'], client['address'], client['registrationDate'], client['invoicing']))

    def insert(self, client):
        self.database.insert(client)
    
    def viewTable(self):
        rows = self.database.getRows()
        clients = []
        for row in rows:
            client = Client(row[0], row[1], row[2], row[3], row[4])
            clients.append(client)
        return clients
    
    def getClient(self, companyName):
        rows = self.database.getRows(companyName)
        if (len(rows) == 0):
            raise FileNotFoundError("This client doesn't exist on the database")
        
        row = rows[0]
        client = Client(row[0], row[1], row[2], row[3], row[4])
        return client
    
    def clientExists(self, companyName):
        try:
            self.getClient(companyName)
            return True
        except:
            return False
    
    def update(self, client):
        properties = {
            'phoneNumber': client.phoneNumber,
            'address': client.address,
            'invoicing': client.invoicing
        }
        key = {
            'companyName': client.companyName
        }
        self.database.update(properties, key)

    def delete(self, companyName):
        self.database.delete({'companyName': companyName})

    def deleteAll(self):
        self.database.deleteAll()

