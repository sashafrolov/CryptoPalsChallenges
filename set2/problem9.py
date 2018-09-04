
def pkcs7(plaintext, blocklength):
  padLength = (blocklength - len(plaintext)%blocklength)%blocklength
  if padLength == 0:
    return plaintext
  
  padChar = chr(padLength)
  padString =padChar * padLength

  paddedText = plaintext + padString
  return paddedText

if __name__ == "__main__":
  print(pkcs7("YELLOW SUBMARINE", 20))