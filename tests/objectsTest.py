from checkpy import *
from _basics import *

@t.test()
def dicerace():
    """dice_race werkt correct"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[10, 6, 1, 2, 4],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(clean_data.strip().split("\n")[-1], 'Game won by Ali!')
    test.test = testMethod
