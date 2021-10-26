import textwrap

def encrypt(message, public_key_n, public_key_e, block_size = 2):
  n = int(public_key_n)
  e = int(public_key_e)

  if len(message) == 0:
    return ""

  # divide message in blocks
  raw_blocks = []
  ciphertext = ord(message[0])
  for i in range(1, len(message)):
    # add ciphertext to the list if block_size is reached, and reset ciphertext
    if (i % block_size == 0):
      raw_blocks.append(ciphertext)
      ciphertext = 0
    # shift by 3 digits and add new charcode
    ciphertext = ciphertext * 1000 + ord(message[i])
  # add the last block to the list
  raw_blocks.append(ciphertext)

  # encrypt all blocks
  encrypted_blocks = [str(pow(block, e, n)) for block in raw_blocks]

  # return encrypted message
  return " ".join(encrypted_blocks)

def decrypt(encoded_message, private_key_n, private_key_d, block_size = 2):
  n = int(private_key_n)
  d = int(private_key_d)

  # list_blocks = textwrap.wrap((encoded_message), block_size)
  list_blocks = encoded_message.split(" ")
  int_blocks = [int(char) for char in list_blocks]

  # decrypt blocks, divide them into chars, and add them to the message
  decrypted_blocks = []
  message = ""
  for block in int_blocks:
    decrypted_block = pow(block, d, n)
    tmp = ""
    for c in range(block_size):
      tmp = chr(decrypted_block % 1000) + tmp
      decrypted_block //= 1000
    message += tmp

  # return decrypted message
  return message
