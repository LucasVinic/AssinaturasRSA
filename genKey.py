import random
from constants import keySize
from auxFunct import mdc, inverModular
from millerMod import genLargePrime

# cria uma chave 
def createKey():
  # gerar dois numeros primos grandes
  np1 = genLargePrime()
  np2 = genLargePrime()
  npAux = np1*np2
  factorCheck = (np1-1)*(np2-1)

  # escolhe numeros pseudo-aleatorios ate que encontre um que é primo com o factorCheck
  while True:
    randNum = random.randrange(pow((keySize-1), 2), pow(keySize, 2))
    if (mdc(randNum, factorCheck) == 1):
      break

  # calcula o inverso multiplicativo modular da key achada, com modulo factorCheck
  randNumInv = inverModular(randNum, factorCheck)
  publKey = (npAux, randNum)
  privKey = (npAux, randNumInv)
  return(publKey, privKey)

createKey()
