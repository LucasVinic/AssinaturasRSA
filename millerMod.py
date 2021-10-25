from constants import lowPrim, keySize
import random

def millerNum(number):
  numberMinus = number - 1
  t = 0
  
  while numberMinus % 2 == 0:
    numberMinus = numberMinus // 2
    t += 1
  for trials in range(5):
    randAux = random.randrange(2, number-1)
    numberPow = pow(randAux, numberMinus, number)
    if numberPow != 1:
      i = 0
      while numberPow != (number-1):
        if i == t - 1:
          return False
        else:
          i = i + 1
          numberPow = (numberPow ** 2) % number
    return True

def isPrime(number):
  if (number < 2):
    return False
  if number in lowPrim:
    return True
  for prime in lowPrim:
    if (number % prime == 0):
      return False
  return millerNum(number)

# gera um numero aleatorio no range, e checa se é primo
def genLargePrime():
  while True:
    number = random.randrange(2**(keySize-1), 2**(keySize))
    if isPrime(number):
      return number