from checkpy import *
from _basics import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def dicerace():
    """dice_race werkt correct"""
    clean_data = outputOf(stdinArgs=[10, 6, 1, 2, 4])
    assert clean_data.strip().split("\n")[-1] == 'Game won by Ali!'
