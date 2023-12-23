from checkpy import *
from _basics import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def dicerace():
    """spel werkt correct zoals voorbeeld in opgave"""
    clean_data = outputOf(stdinArgs=[10, 6, 1, 2, 4], overwriteAttributes=[("__name__", "__main__")])
    assert clean_data.strip().split("\n")[-1].strip() == 'Game won by Ali!'
