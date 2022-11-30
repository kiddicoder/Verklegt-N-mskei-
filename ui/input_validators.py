class NameLengthException(Exception):
  pass


class NotANumber(Exception):
  pass


def name_validator(name):
  if len(name) >= 50:
    raise NameLengthException


def id_validator(id):
  print("ég er í id")
  if len(id) != 10:
    raise NameLengthException()
  if id.isdigit() == False:
    raise NotANumber


def address_validator(address):
  print("ég er í address")
  if len(address) >= 25:
    raise NameLengthException


def phone_validator(phone):  #á líka við gsm
  print("ég er í phone")
  if len(phone) != 7:
    raise NameLengthException  #kannski búa til nýtt exception?
  if phone.isdigit() == False:
    raise NotANumber


def email_validator(email):
  print("ég er í email")
  if len(email) >= 25:
    raise NameLengthException


def role_validator(role):
  print("ég er í role")
  role = role.strip()
  role = role.islower()
  if role != 'player' and role != 'captain':
    raise SyntaxError