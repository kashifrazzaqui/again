import os
import binascii
import re


def unique_hex(byte_length=4):
    return binascii.hexlify(os.urandom(byte_length)).decode()


def natural_sort(item):
    """
    Sort strings that contain numbers correctly.

    >>> l = ['v1.3.12', 'v1.3.3', 'v1.2.5', 'v1.2.15', 'v1.2.3', 'v1.2.1']
    >>> l.sort(key=natural_sort)
    >>> print l
    "['v1.2.1', 'v1.2.3', 'v1.2.5', 'v1.2.15', 'v1.3.3', 'v1.3.12']"
    """
    if item is None:
        return 0

    def try_int(s):
        try:
            return int(s)
        except ValueError:
            return s
    return tuple(map(try_int, re.findall(r'(\d+|\D+)', item)))


if __name__ == '__main__':
    print(unique_hex())

