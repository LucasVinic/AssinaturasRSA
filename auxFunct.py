# calculo do Máximo Divisor Comum
def mdc(x, y):
  if (y == 0):
    return x
  ret = x % y
  return mdc(y, ret)

# calculo do inverso multiplicativo modular 
def inverModular(x, y):
  if mdc(x, y) != 1:
    return None
  u1, u2, u3 = 1, 0, x
  v1, v2, v3 = 0, 1, y
  
  while v3 != 0:
    q = u3 // v3
    v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
  return u1 % y