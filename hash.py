import hashlib

def hashMessage(str):
  return hashlib.sha3_512(str.encode()).hexdigest()
