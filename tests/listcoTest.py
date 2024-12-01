from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def som_lengte():
    """som_lengte werkt correct"""
    assert defines_function("som_lengte")
    assert getFunction("som_lengte")(["apple", "orange", "pear"]) == 15
    assert getFunction("som_lengte")([""]) == 0
    assert getFunction("som_lengte")([]) == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def filter_apples():
    """filter_apples werkt correct"""
    assert defines_function("filter_apples")
    assert getFunction("filter_apples")(['X', 'Android', 'iPad', '_underscore.js', 'iPod', 'ChatGPT', '3D Studio Max', 'macOS', '.Net']) == ['X', 'Android', '_underscore.js', 'ChatGPT', '3D Studio Max', '.Net']
    assert getFunction("filter_apples")(['iPad']) == []
    assert getFunction("filter_apples")([]) == []

@t.passed(no_syntax_error, hide=False)
@t.test()
def zonder_klinkers():
    """zonder_klinkers werkt correct"""
    assert defines_function("zonder_klinkers")
    assert getFunction("zonder_klinkers")(["apple", "orange", "pear"]) == ['ppl', 'rng', 'pr']
    assert getFunction("zonder_klinkers")(["apples"]) == ['ppls']
    assert getFunction("zonder_klinkers")([]) == []

@t.passed(no_syntax_error, hide=False)
@t.test()
def multiples_of_three():
    """multiples_of_three werkt correct"""
    assert defines_function("multiples_of_three")
    assert getFunction("multiples_of_three")([1, 3, 4, 6, 9, 11]) == [3, 6, 9]
    assert getFunction("multiples_of_three")([9, 6]) == [9, 6]
    assert getFunction("multiples_of_three")([]) == []
