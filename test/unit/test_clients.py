import unittest
import json
from database.client_db import ClientDatabase
from test.unit.base_case import BaseCase

class ClientsTest(BaseCase):
    def setUp(self):
        self.db = ClientDatabase()
        super().setUp()
        self.payloadJson['companyName'] = "TESTE_2"
        self.payload = json.dumps(self.payloadJson)

    def test_successful_insertion(self):
        # Given
        payload = self.payload
        companyName = self.payloadJson['companyName']

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(companyName, response.json['companyName'])
        self.assertEqual(200, response.status_code)
        self.assertTrue(self.db.clientExists(companyName))
    
    def test_duplicate_insertion(self):
        # Given
        payload = self.payload

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
    
    def test_invalid_phone_number(self):
        # Given
        self.payloadJson["phoneNumber"] = "9998334"
        payload = json.dumps(self.payloadJson)

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
        self.assertFalse(self.db.clientExists(self.payloadJson['companyName']))
    
    def test_invalid_date(self):
        # Given
        self.payloadJson["registrationDate"] = "20000000"
        payload = json.dumps(self.payloadJson)

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
        self.assertFalse(self.db.clientExists(self.payloadJson['companyName']))
    
    def test_invalid_invoicing(self):
        # Given
        self.payloadJson["invoicing"] = "aaaa"
        payload = json.dumps(self.payloadJson)

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
        self.assertFalse(self.db.clientExists(self.payloadJson['companyName']))
    
    def test_invalid_request(self):
        # Given
        self.payloadJson["bankAccounts"] = None
        payload = json.dumps(self.payloadJson)
        
        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
        self.assertFalse(self.db.clientExists(self.payloadJson['companyName']))
    
    def test_invalid_bankAccount(self):
        # Given
        bankAccount = {
            "codeBank": "0080",
            "agencyNumber": "00404"
            #missing account number
        }
        self.payloadJson["bankAccounts"] = [bankAccount]
        payload = json.dumps(self.payloadJson)

        # When
        response = self.app.post('/clients', headers={"Content-Type": "application/json"}, data=payload)

        # Then
        self.assertEqual(400, response.status_code)
        self.assertFalse(self.db.clientExists(self.payloadJson['companyName']))
    
    def test_get(self):
        # When
        response = self.app.get('/clients', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(list, type(response.json))
    
    def tearDown(self):
        self.db.delete("TESTE_2")
        super().tearDown()