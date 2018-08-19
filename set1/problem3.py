import base64
import string
def hexStringtoBytes(hexstring):
    byteArray = bytes.fromhex(hexstring)
    return byteArray

def xorBytes(bytes1, bytes2):
    xored = bytes([x^bytes2[i] for i,x in enumerate(bytes1)])
    return xored

def xorAgainstCharacter(byteArray, character):
    str2 = [ord(character)] * len(byteArray)
    return xorBytes(byteArray,str2)

def scoreString(input):
    arr = [(chr(x) in string.printable) for x in input]
    return arr.count(True)

if __name__ == "__main__":
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    bytes1 = hexStringtoBytes(hexstring)
    scores = []
    for x in string.printable:
        temp = xorAgainstCharacter(bytes1, x)
        print(str(x), str(temp))
        scores.append(scoreString(temp))
