import base36
import base58
import base62
import base64
import base91
#import base92
import base128
import binascii


def get_return(i,xx):
    temp =  i(xx)
    if type(temp) == int:
        temp= binascii.a2b_hex(hex(temp)[2:].encode())
    return temp+(" |"+i.__name__).encode()+"\x0a".encode()

def main(xx):

    func=[base64.b16decode,
            base64.b32decode,
            base36.loads,
            base58.b58decode,
            base62.decodebytes,
            base64.b64decode,
            base64.b85decode,
            base91.decode,
            ]

    result =b""

    for i in func:
        try:
            result += get_return(i,xx)
        except:
            pass
   
    print(result)
    i=base128.decode
    result = get_return(i,xx)
    print(result)



main("MZYVMIWLGBL7CIJOGJQVOA3IN5BLYC3NHI")