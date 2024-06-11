import utils.file as file
import os

from test.basics import test as test_input
from test.middle import test as test_middle

def test():
    test_input()
    # test_middle()
    print("All tests passed successfully...")

if __name__ == "__main__":
    test()