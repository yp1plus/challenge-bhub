import json
from database.client_db import ClientDatabase
from database.bankAccount_db import BankAccountDatabase
from test.unit.base_case import BaseCase

class ClientTest(BaseCase):
    def setUp(self):
        self.db = ClientDatabase()
        self.bankAccount_db = BankAccountDatabase()
        super(ClientTest, self).setUp()

    def test_successful_update(self):
        # Given
        payload = json.dumps({
            "address": "RUA CARDEAL ARCOVERDE",
        })

        # When
        response = self.app.put(f'/clients/{self.payloadJson["companyName"]}', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual("RUA CARDEAL ARCOVERDE", response.json['address'])
        self.assertEqual(200, response.status_code)
    
    def test_unsuccessful_update(self):
        # Given
        companyName = self.payloadJson["companyName"]
        payload = None

        # When
        response = self.app.put(f'/clients/{companyName}', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
    
    def test_successful_update_ignoring_fields(self):
        # Given
        payload = json.dumps({
            "companyName": "LALALA",
            "phoneNumber": "(11) 93945-3065",
            "address": "RUA CARDEAL ARCOVERDE, 2365 - 3ºANDAR | SÃO PAULO - SP - CEP: 05407-003",
            "registrationDate": "03/04/2020",
            "invoicing": "500000",
            "bankAccounts": []
        })
        companyName = self.payloadJson["companyName"]

        # When
        response = self.app.put(f'/clients/{companyName}', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertNotEqual("LALALA", companyName) #ignores anything not updatable 
        self.assertEqual(200, response.status_code)
    
    def test_get(self):
        # Given
        companyName = self.payloadJson["companyName"]

        # When
        response = self.app.get(f'/clients/{companyName}', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(companyName, response.json['companyName'])
    
    def test_delete(self):
        # Given
        companyName = self.payloadJson["companyName"]

        # When
        response = self.app.delete(f'/clients/{companyName}', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)
        self.assertFalse(self.db.clientExists(companyName))
        self.assertEqual(0, len(self.bankAccount_db.getBankAccounts(companyName)))