"""Showing context managers example."""
from contextlib import contextmanager


class Frame:
    """Creating Frame class."""
    def __enter__(self):
        print("entering")

    def __exit__(self, *args):
        print("exiting")

@contextmanager
def frame():
    print("entering")
    try:
        yield
    finally:
        print("exiting")

def gen_ints():
    i = 0
    while True:
        yield i
        i += 1


if __name__ == "__main__":
    with frame():
        print("I'm in a frame!")
    #with Frame
    #    print("I'm in a Frame!")
