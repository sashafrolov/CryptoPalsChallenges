def repeatingKeyXOR(plaintext, key):
    keylen = len(key)
    encrypted = []
    for i,x in enumerate(plaintext):
        encryptedByte = ord(x) ^ ord(key[i%keylen])
        encrypted.append(encryptedByte)
    return bytes(encrypted)

plaintext = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

print(repeatingKeyXOR(plaintext, 'ICE').hex())
