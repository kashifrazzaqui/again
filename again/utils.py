import os, binascii

def unique_hex(length=8):
    return binascii.hexlify(os.urandom(int(length/2))).decode()


if __name__ == '__main__':
    print(unique_hex())

