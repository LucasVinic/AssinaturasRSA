#! /usr/bin/python3
import sys
from crypt import encrypt, decrypt

# usage:
#  chmod +x main.py
#  ./main.py ./arquivo.txt

if __name__ == "__main__":
  # inputFilename = sys.argv[1]

  # inputFile = open(inputFilename, 'r', encoding='utf-8')
  # fileContents = inputFile.read()
  # inputFile.close()
  # print(f'Read file "{inputFilename}" successfully')
  
  # Generate hash for input file contents
  # rawContentHash = ???????
  # print(f'Generated hash for "{inputFilename}": {rawContentHash}')

  # Encode file contents with public key
  # encodedContent = ?????????
  # print(f'Encoded file contents for "{inputFilename}"')

  # Decode file contents with private key
  # decodedContent = ?????????
  # print(f'Decoded file contents for "{inputFilename}"')

  # Generate hash for decoded file contents
  # decodedContentHash = ???????
  # print(f'Generated hash for decoded "{inputFilename}": {decodedContentHash}')

  # Compare hashes of original and decoded file contents
  # hashesAreEqual = ??????????
  # print(f'Hashes for raw and decoded content are equal? {hashesAreEqual}')

  # test keys
  n = 2214347
  e = 2057363
  d = 905627

  message = "AEEE tá funcionando!!!çãé@#$%"
  print(f'raw message {message}')
  encrypted = encrypt(message, n, e)
  print(f'encrypted {encrypted}')
  decrypted = decrypt(encrypted, n, d)
  print(f'decrypted {decrypted}')
