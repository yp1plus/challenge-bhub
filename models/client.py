import json

class Client:
  def __init__(self, companyName, phoneNumber, address, registrationDate, invoicing):
    self.companyName = companyName
    self.phoneNumber = phoneNumber
    self.address = address
    self.registrationDate = registrationDate
    self.invoicing = invoicing
  
  def values(self):
    return [self.companyName, self.phoneNumber, self.address, self.registrationDate, self.invoicing]

  def serialize(self):
    return json.dumps({
      'companyName': self.companyName,
      'phoneNumber': self.phoneNumber,
      'address': self.address,
      'registrationDate': self.registrationDate,
      'invoicing': self.invoicing,
    })