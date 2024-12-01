from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def word_frequencies():
    """word_frequencies werkt correct"""
    assert defines_function("word_frequencies")
    assert getFunction("word_frequencies")("Hello world hello") == {'hello': 2, 'world': 1}
    assert getFunction("word_frequencies")("") == {}
    assert getFunction("word_frequencies")("hoi hoi") == { 'hoi': 2}

@t.passed(no_syntax_error, hide=False)
@t.test()
def dict_intersect():
    """dict_intersect werkt correct"""
    assert defines_function("dict_intersect")
    assert getFunction("dict_intersect")({ 'a': 1, 'b': 2, 'c': 3 }, { 'a': 2, 'b': 2, 'd': 3 }) == { 'b': 2 }
    assert getFunction("dict_intersect")({}, {}) == {}

@t.passed(no_syntax_error, hide=False)
@t.test()
def inverse_points():
    """inverse_points werkt correct"""
    assert defines_function("inverse_points")
    assert getFunction("inverse_points")() == {1: ('a', 'e', 'n', 'o'), 3: ('b', 'g', 'k', 'l', 'm', 'p'), 5: ('c', 'w'), 2: ('d', 'i', 'r', 's', 't'), 4: ('f', 'h', 'j', 'u', 'v', 'z'), 10: ('q',), 8: ('x', 'y')}
