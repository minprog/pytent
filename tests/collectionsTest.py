from checkpy import *
from _basics import *
from _static_analysis import *

@t.test()
def emmeren():
    """emmeren werkt correct"""
    assert defines_function("emmeren")
    assert getFunction("emmeren")([[1,2,3], [3,4], [4,5]]) == {3: [[1, 2, 3]], 2: [[3, 4], [4, 5]]}

@t.test()
def maak_overzicht():
    """maak_overzicht werkt correct"""
    assert defines_function("maak_overzicht")
    assert getFunction("maak_overzicht")([(2, 3, 0), (3, 0, 0)]) == {"cola": 5, "sinas": 3, "limonade": 0}

@t.test()
def rits():
    """rits werkt correct"""
    assert defines_function("rits")
    assert getFunction("rits")([1, 2, 3], [2, 4, 4]) == [(1, 2), (3, 4)]
    assert getFunction("rits")([10, 30, 50, 70], [10, 20]) == [(10, 10)]
    assert getFunction("rits")([5, 7, 9], []) == []
