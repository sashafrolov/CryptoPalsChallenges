import base64
def hexStringtoBase64String(hexstring):
    byteArray = bytes.fromhex(hexstring)
    return str(base64.b64encode(byteArray))[2:-1]


if __name__ == '__main__':
    hexstring = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(str(hexStringtoBase64String(hexstring)))
