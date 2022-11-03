import code
import json
from uuid import uuid4

class BankAccount:
  def __init__(self, id, companyName, codeBank, agencyNumber, accountNumber):
    self.id = id or uuid4().__str__()
    self.companyName = companyName
    self.codeBank = codeBank
    self.agencyNumber = agencyNumber
    self.accountNumber = accountNumber
  
  def values(self):
    return [self.id, self.companyName, self.codeBank, self.agencyNumber, self.accountNumber]

  def serialize(self):
    return {
      'id': self.id,
      'companyName': self.companyName,
      'codeBank': self.codeBank,
      'agencyNumber': self.agencyNumber,
      'accountNumber':self.accountNumber
    }