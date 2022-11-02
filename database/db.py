import sqlite3

class Database:
    def __init__(self, tableName):
        self.connection = sqlite3.connect('bhub.db')
        self.cursor = self.connection.cursor()
        self.tableName = tableName
        
    def executeFunction(self, function):
        self.connection = sqlite3.connect('bhub.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(function)
    
    def closeConnection(self):
        self.connection.commit()
        self.connection.close()
    
    def makeFullRequest(self, function):
        self.executeFunction(function)
        self.closeConnection()
        
    def insert(self, object):
        array = []
        for value in object.values():
            if type(value) == str:
                array.append('\'' + value + '\'')
            else:
                array.append(str(value))
        values = ','.join(array)
        values = '(' + values + ')'
        self.makeFullRequest(f"INSERT INTO {self.tableName} VALUES {values}")
    
    def getRows(self):
        self.executeFunction(f"SELECT * FROM {self.tableName}")
        rows = self.cursor.fetchall()
        self.closeConnection()

        return rows
    
    def getRow(self, key):
        self.executeFunction(f"SELECT * FROM {self.tableName} WHERE {self.generateKeyStatement(key)}")
        row = self.cursor.fetchone()
        if (row == None):
            raise FileNotFoundError("This object doesn't exist on the database")
        self.closeConnection()

        return row
    
    def update(self, properties, key):
        values = ','.join([f'{item}={properties[item]}' for item in properties])
        self.makeFullRequest(f"UPDATE {self.tableName} SET {values} WHERE {self.generateKeyStatement(key)}")
    
    def delete(self, key):
        self.makeFullRequest(f"DELETE FROM {self.tableName} WHERE {self.generateKeyStatement(key)}")
    
    def deleteAll(self):
        self.makeFullRequest(f"DELETE FROM {self.tableName}")
    
    def generateKeyStatement(self, key):
        for x, y in key.items():
            return f"{x}=\'{y}\'"