import base64
import string
def base64stringtoBytes(s):
    return base64.b4decode(s)

def hammingDistance(bytes1,bytes2):
    hammingDist = 0
    for i,x in enumerate(bytes1):
        numEdits = x ^ bytes2[i]
        zeroOnes = bin(numEdits)[2:].zfill(8)
        hammingDist += zeroOnes.count('1')
    return hammingDist

#print(hammingDistance(bytes('this is a test', 'ascii'),bytes('wokka wokka!!!', 'ascii')))
f = open("6.txt").readlines()
decoded = base64.b64decode(''.join(f))
normalizedKeySizeDistances ={}
for keysize in range(2,41):
    distance = hammingDistance(decoded[0:keysize],decoded[keysize:2*keysize])
    normalizedKeySizeDistances[str(keysize)] = distance/keysize


keysize = 29

from collections import defaultdict
blocks = defaultdict(list)
for i,x in enumerate(decoded):
    blocks[str(i%keysize)].append(x)

def xorBytes(bytes1, bytes2):
    xored = bytes([x^bytes2[i] for i,x in enumerate(bytes1)])
    return xored

def xorAgainstCharacter(byteArray, character):
    str2 = [ord(character)] * len(byteArray)
    return xorBytes(byteArray,str2)

def scoreString(input):
    arr = [(chr(x) in 'ETAOIN SHRDLU etaoin shrdlu') for x in input]
    return arr.count(True)

for x in blocks:
    blocks[x] = bytes(blocks[x])

scores = defaultdict(dict)
for x in blocks:
    for y in string.printable:
        temp = xorAgainstCharacter(blocks[x], y)
        scores[x][y] = scoreString(temp)

def repeatingKeyXOR(plaintextbytes, key):
    keylen = len(key)
    encrypted = []
    for i,x in enumerate(plaintextbytes):
        encryptedByte = x ^ ord(key[i%keylen])
        encrypted.append(encryptedByte)
    return bytes(encrypted)

print(str(repeatingKeyXOR(decoded, 'nonnn')))
