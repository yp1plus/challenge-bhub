import json
import unittest
from app import app

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.payload = json.dumps({
            "companyName": "TESTE",
            "phoneNumber": "(11) 93945-3065",
            "address": "RUA CARDEAL ARCOVERDE, 2365 - 3ºANDAR | SÃO PAULO - SP - CEP: 05407-003",
            "registrationDate": "01/02/2020",
            "invoicing": "500000",
            "bankAccounts": [{
                "agencyNumber": "000304",
                "accountNumber": "9292393",
                "codeBank": "0040"
            }]
        })
        self.payloadJson = json.loads(self.payload)
        self.app.post('/clients', headers={"Content-Type": "application/json"}, data=self.payload)
        
    def tearDown(self):
        self.app.delete('/clients/TESTE', headers={"Content-Type": "application/json"})