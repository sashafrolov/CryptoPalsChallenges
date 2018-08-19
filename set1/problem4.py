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

f= open('4.txt')
encodedStrings = list(f)
encodedStrings = [hexStringtoBytes(x.strip()) for x in encodedStrings]
maxScores = []
decryptedStrings = []
correspondingArray = []
for x in encodedStrings:
    scores = []
    for y in string.printable:
        temp = xorAgainstCharacter(x, y)
        scores.append(scoreString(temp))
        if scoreString(temp) == 30:
            decryptedStrings.append(temp)
            correspondingArray.append((x,y))
    print(max(scores), x)
    maxScores.append(max(scores))
