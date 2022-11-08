import json
from database.bankAccount_db import BankAccountDatabase
from test.unit.base_case import BaseCase

class BankAccountsTest(BaseCase):
    def setUp(self):
        self.db = BankAccountDatabase()
        super().setUp()
        
    def test_successful_insertion(self):
        # Given
        payload = json.dumps({
            "codeBank": "00890",
            "agencyNumber": "0080",
            "accountNumber": "1501476513"
        })

        # When
        response = self.app.post(f'/clients/{self.payloadJson["companyName"]}/bankAccounts', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
    
    def test_unsuccessful_insertion(self):
        # Given
        payload = json.dumps({
            "codeBank": "00890",
            "agencyNumber": "0080",
            "accountNumber": "1501476513"
        })
        wrongCompanyName = "wrong"

        # When
        response = self.app.post(f'/clients/{wrongCompanyName}/bankAccounts', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
    
    def test_get(self):
        # When
        response = self.app.get(f'/clients/{self.payloadJson["companyName"]}/bankAccounts', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(response.json), 0)