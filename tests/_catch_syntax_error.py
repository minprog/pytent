import checkpy.tests as t

from _static_analysis import *

@t.test(1)
def no_syntax_error(test):
    """het bestand is in orde"""
    def testMethod():
        if lineno := has_syntax_error():
            return False, f"de code bevat een syntax error op regel {lineno}"
        return True
    test.test = testMethod
