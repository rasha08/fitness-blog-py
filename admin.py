import hashlib

hash = 'ddee9363c28745f4982179cc35f03fb59d6e924a3ce7c49a53813594917a1c37';

def loginAdmin(data):
  formData = data.to_dict()
  if not formData['password']:
    return None
  elif formData['password'] and checkPassword(formData['password']):
    return 'success'
  else:
    return None

def checkPassword(password):
  hashedPassword = hashlib.sha256(password.encode('utf-8'))
  return hashedPassword.hexdigest() == hash