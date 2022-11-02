import json
import phonenumbers
from dateutil import parser

class Client:
  def __init__(self, companyName, phoneNumber, address, registrationDate, invoicing):
    self.companyName = companyName
    self.phoneNumber = self.validatePhoneNumber(phoneNumber)
    self.address = address
    self.registrationDate = self.validateDate(registrationDate)
    self.invoicing = self.validateNumber(invoicing)
  
  def validatePhoneNumber(phoneNumber):
    number = phonenumbers.parse(phoneNumber)
    if (phonenumbers.is_valid_number(number)):
      return phoneNumber
    else:
      raise ValueError("phone number is invalid")
  
  def validateDate(registrationDate):
    try:
      parser.parse(registrationDate)
      return registrationDate
    except ValueError:
      raise ValueError("date format is invalid")
  
  def validateNumber(invoicing):
    try:
      return float(invoicing)
    except ValueError:
      raise ValueError("Invoicing is not a number")

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