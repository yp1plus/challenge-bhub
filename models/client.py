import phonenumbers
from dateutil import parser

class Client:
  def __init__(self, companyName, phoneNumber, address, registrationDate, invoicing):
    self.companyName = companyName
    self.phoneNumber = self.validatePhoneNumber(phoneNumber)
    self.address = address
    self.registrationDate = self.validateDate(registrationDate)
    self.invoicing = self.validateNumber(invoicing)
  
  def setPhoneNumber(self, phoneNumber):
    self.phoneNumber = self.validatePhoneNumber(phoneNumber)
  
  def setInvoicing(self, invoicing):
    self.invoicing = self.validateNumber(invoicing)
  
  def setAddress(self, address):
    self.address = address

  def validatePhoneNumber(self, phoneNumber):
    number = phonenumbers.parse(phoneNumber, 'BR')
    if (phonenumbers.is_valid_number(number)):
      return phoneNumber
    else:
      raise ValueError("Phone number is invalid")
  
  def validateDate(self, registrationDate):
    try:
      parser.parse(registrationDate)
      return registrationDate
    except ValueError:
      raise ValueError("Date format is invalid")
  
  def validateNumber(self, invoicing):
    try:
      return float(invoicing)
    except ValueError:
      raise ValueError("Invoicing is not a number")

  def values(self):
    return [self.companyName, self.phoneNumber, self.address, self.registrationDate, self.invoicing]

  def serialize(self):
    return {
      'companyName': self.companyName,
      'phoneNumber': self.phoneNumber,
      'address': self.address,
      'registrationDate': self.registrationDate,
      'invoicing': self.invoicing,
    }