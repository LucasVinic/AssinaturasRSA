import random
from constants import np1, np2, npAux, factorCheck, keySize
from auxFunct import mdc, inverModular

# cria uma chave 
def createKey():

  # escolhe numeros pseudo-aleatorios ate que encontre um que é primo com o factorCheck
  while True:
    randNum = random.randrange(2**(keySize-1), 2**keySize)
    if (mdc(randNum, factorCheck) == 1):
      break

  # calcula o inverso multiplicativo modular da key achada, com modulo factorCheck
  randNumInv = inverModular(randNum, factorCheck)
  publKey = (npAux, randNum)
  privKey = (npAux, randNumInv)
  print(f'chave publica {publKey}.')
  print(f'chave privada {privKey}.')
  return(publKey, privKey)

createKey()
