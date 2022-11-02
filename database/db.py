import sqlite3

class Database:
    def __init__(self, tableName):
        self.connection = sqlite3.connect('bhub.db')
        self.cursor = self.connection.cursor()
        self.tableName = tableName
        
    def executeFunction(self, function):
        self.cursor.execute(function)
        self.connection.commit()
        self.connection.close()
    
    def insert(self, object):
        values = ','.join([str(value) for value in object.values()])
        values = '(' + values + ')'
        self.executeFunction(f"INSERT INTO {self.tableName} VALUES {values}")
    
    def getRows(self):
        self.executeFunction(f"SELECT * FROM {self.tableName}")
        rows = self.cursor.fetchall()

        return rows
    
    def getRows(self, key):
        self.executeFunction(f"SELECT * FROM {self.tableName} WHERE {self.generateKeyStatement(key)}")
        rows = self.cursor.fetchall()

        return rows
    
    def update(self, properties, key):
        values = ','.join([f'{item}={properties[item]}' for item in properties])
        self.executeFunction(f"UPDATE {self.tableName} SET {values} WHERE {self.generateKeyStatement(key)}")
    
    def delete(self, key):
        self.executeFunction(f"DELETE FROM {self.tableName} WHERE {self.generateKeyStatement(key)}")
    
    def generateKeyStatement(key):
        return f'{key.keys()[0]}={key.values()[0]}'

    def deleteAll(self):
        self.executeFunction(f"DELETE FROM {self.tableName}")