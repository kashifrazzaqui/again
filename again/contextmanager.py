import time
from contextlib import contextmanager

@contextmanager
def timethis(label, receiver_fn=None):
    """ Times a block of code
    Inspired from David Beazley talk - Generators: The Final Frontier"""

    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        if receiver_fn:
            receiver_fn(label, start, end)
        else:
            print('{}: {} to {} -> {} seconds'.format(label, start, end, end-start))
