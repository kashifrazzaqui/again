import os, binascii

def unique_hex(byte_length=4):
    return binascii.hexlify(os.urandom(byte_length)).decode()


if __name__ == '__main__':
    print(unique_hex())

