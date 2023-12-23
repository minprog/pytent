from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def deelbaar():
    """deelbaar werkt correct"""
    assert defines_function("deelbaar")
    assert getFunction("deelbaar")([10, 15, 20, 25, 100], 10) == [10, 20, 100]

@t.passed(no_syntax_error, hide=False)
@t.test()
def oeps():
    """oeps werkt correct"""
    assert defines_function("oeps")
    assert getFunction("oeps")(["dit", "was", "een", "lijst", "van", "woorden"]) == ["dit", "oeps", "een", "oeps", "van", "oeps"]

@t.passed(no_syntax_error, hide=False)
@t.test()
def schreeuw():
    """schreeuw werkt correct"""
    assert defines_function("schreeuw")
    assert getFunction("schreeuw")("dit is een zin") == 'diiiiit iiiiis eeeeeeeeeen ziiiiin'

@t.passed(no_syntax_error, hide=False)
@t.test()
def ketting():
    """ketting werkt correct"""
    assert defines_function("ketting")
    assert getFunction("ketting")([[1, 2], [2, 3], [3, 4]]) == [[1, 2], [2, 3]]
    assert getFunction("ketting")([[1, 7], [2, 3], [3, 4]]) == [[2, 3]]
    assert getFunction("ketting")([[1, 2]]) == []
