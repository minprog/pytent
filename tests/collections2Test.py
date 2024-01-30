from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_products():
    """get_products werkt correct"""
    assert defines_function("get_products")
    products = [('snoep', 'drop', 1.45),
                ('snoep', 'banaantjes', 2.05),
                ('groente', 'ui', 0.55),
                ('groente', 'yacon', 5.09)]
    assert getFunction("get_products")(products, 'groente', 3) == ['ui']
    assert getFunction("get_products")(products, 'groente', 0) == []

@t.passed(no_syntax_error, hide=False)
@t.test()
def reverse_dict():
    """reverse_dict werkt correct"""
    assert defines_function("reverse_dict")
    assert getFunction("reverse_dict")({ 1: 'one', 2: 'two', 3: 'three' }) == { 'one': 1, 'two': 2, 'three': 3 }
    assert getFunction("reverse_dict")({ 3: 'one', 2: 'two', 1: 'three' }) == { 'one': 3, 'two': 2, 'three': 1 }

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_valid_dance():
    """is_valid_dance werkt correct"""
    assert defines_function("is_valid_dance")
    assert getFunction("is_valid_dance")([ ("R", 2) ]) == False
    assert getFunction("is_valid_dance")([ ("R", 2), ("L", 2) ]) == True
    assert getFunction("is_valid_dance")([ ("R", 2), ("V", 2), ("L", 2), ("A", 2) ]) == True
