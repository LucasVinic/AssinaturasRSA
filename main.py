#! /usr/bin/python3
import sys
from crypt import encrypt, decrypt

from hash import hashMessage
from auxFunct import processString
from genKey import createKey

# usage:
#  chmod +x main.py
#  ./main.py ./arquivo.txt

def main():
  # Parse args
  inputFilename = sys.argv[1]

  # Read input file
  inputFile = open(inputFilename, 'r', encoding='utf-8')
  fileContents = inputFile.read()
  inputFile.close()
  print(f'Read file "{inputFilename}" successfully')

  # Generate private and public keys
  (publKey, privKey) = createKey()
  (n, e) = publKey
  (n, d) = privKey

  # Generate hash for input file contents
  rawContentHash = hashMessage(fileContents)
  print(f'Generated hash for "{inputFilename}": {rawContentHash}')

  # Encode file contents with public key
  encodedContent = encrypt(fileContents, n, e)
  print(f'Encoded file contents for "{inputFilename}"')

  # Decode file contents with private key
  decodedContent = decrypt(encodedContent, n, d)
  print(f'Decoded file contents for "{inputFilename}"')

  # Generate hash for decoded file contents
  decodedContentHash = hashMessage(fileContents)
  print(f'Generated hash for decoded "{inputFilename}": {decodedContentHash}')

  # Compare hashes of original and decoded file contents
  hashesAreEqual = rawContentHash == decodedContentHash
  print(f'Hashes for raw and decoded content are equal? {hashesAreEqual}')

if __name__ == "__main__":
  main()
