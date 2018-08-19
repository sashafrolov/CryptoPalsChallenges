import base64
def hexStringtoBytes(hexstring):
    byteArray = bytes.fromhex(hexstring)
    return byteArray

def xorByes(bytes1, bytes2):
    xored = bytes([x^bytes2[i] for i,x in enumerate(bytes1)])
    return xored

if __name__ == '__main__':
    str1 = hexStringtoBytes('1c0111001f010100061a024b53535009181c')
    str2 = hexStringtoBytes('686974207468652062756c6c277320657965')
    str3 = bytes([x^str2[i] for i,x in enumerate(str1)])
    print(str3.hex())
