import code
import json
from uuid import uuid4


class BankAccount:
  def __init__(self, companyName, codeBank, agencyNumber, accountNumber):
    self.id = uuid4().__str__()
    self.companyName = companyName
    self.codeBank = codeBank
    self.agencyNumber = agencyNumber
    self.accountNumber = accountNumber

  def serialize(self):
    return json.dumps({
      'id': self.id,
      'companyName': self.companyName,
      'codeBank': self.codeBank,
      'agencyNumber': self.agencyNumber,
      'accountNumber':self.accountNumber
    })