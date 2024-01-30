from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def namen():
    """namen werkt correct"""
    assert defines_function("namen")
    assert getFunction("namen")(['Felix', 'rubric', 'Mo', 'Kim', 'Felicity', 'onder', 'kind', 'Ferdinand']) == ['felix', 'mo', 'kim', 'felicity', 'ferdinand']

@t.passed(no_syntax_error, hide=False)
@t.test()
def add_numbers():
    """add_numbers werkt correct"""
    assert defines_function("add_numbers")
    assert getFunction("add_numbers")(['these', 'stories', 'wear', 'scars', 'stretchmarks', 'wrinkles']) == ['1. these', '2. stories', '3. wear', '4. scars', '5. stretchmarks', '6. wrinkles']
    assert getFunction("add_numbers")(['wrinkles']) == ['1. wrinkles']

@t.passed(no_syntax_error, hide=False)
@t.test()
def replace_specials():
    """replace_specials werkt correct"""
    assert defines_function("replace_specials")
    assert getFunction("replace_specials")('hello, world!') == 'hello__world_'
    assert getFunction("replace_specials")('A') == 'A'
    assert getFunction("replace_specials")('@@@') == '___'

@t.passed(no_syntax_error, hide=False)
@t.test()
def volgorde():
    """volgorde werkt correct"""
    assert defines_function("volgorde")
    assert getFunction("volgorde")([1, 5, 4, 4, 1]) == [1, 5]
    assert getFunction("volgorde")([10]) == [10]
    assert getFunction("volgorde")([5, 4, 6, 7, 8]) == [5, 6, 7, 8]
