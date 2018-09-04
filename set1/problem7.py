from Crypto.Cipher import AES
from Crypto import Random
import base64

def decryptFile(key, cipherText):
  decryptor = AES.new(key, AES.MODE_ECB)
  return decryptor.decrypt(cipherText)

if __name__ == "__main__":
  toDecrypt = open("7.txt").read()
  toDecrypt = base64.b64decode(toDecrypt)
  print(decryptFile("YELLOW SUBMARINE", toDecrypt))