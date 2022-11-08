from database.bankAccount_db import BankAccountDatabase
from test.unit.base_case import BaseCase

class BankAccountTest(BaseCase):
    def setUp(self):
        self.db = BankAccountDatabase()
        super(BankAccountTest, self).setUp()

    def test_delete(self):
        # Given
        bankAccounts = self.db.getBankAccounts(self.payloadJson["companyName"])
        id = bankAccounts[0]["id"]

        # When
        response = self.app.delete(f'/clients/bankAccounts/{id}', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)
        with self.assertRaises(FileNotFoundError):
            self.db.getBankAccount(id) 
    
    def test_get_with_inexistent(self):
        # Given
        wrongId = "wrong"

        # When
        response = self.app.get(f'/clients/bankAccounts/{wrongId}', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(400, response.status_code)
        self.assertEqual("This object doesn't exist on the database", response.json)
    
    def test_get(self):
        # Given
        bankAccounts = self.db.getBankAccounts(self.payloadJson["companyName"])
        id = bankAccounts[0]["id"]
        
        # When
        response = self.app.get(f"/clients/bankAccounts/{id}", headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)