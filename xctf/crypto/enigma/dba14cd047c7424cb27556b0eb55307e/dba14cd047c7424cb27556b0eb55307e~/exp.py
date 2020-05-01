import codecs
from crypto_commons.generic import chunk_with_remainder, xor_string


def main():
    cts = []
    for i in range(1, 7):
        with codecs.open("encrypted/" + str(i) + "e", "r") as input_file:
            data = input_file.read().strip()
            data = xor_string(chr(ord('&') ^ ord(' ')) * len(data), data)
            print(chr(ord('&') ^ ord(' ')) * len(data))

            cts.append(data)
    print(cts)



main()