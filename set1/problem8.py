import base64

toDecrypt = open("8.txt").readlines()
toDecrypt = [bytes.fromhex(x[0:320]) for x in toDecrypt]

for x in toDecrypt:
    blocks = [x[i:i+16] for i in range(0,len(x),16)]
    if len(blocks) != len(set(blocks)):
        print(x, toDecrypt.index(x))