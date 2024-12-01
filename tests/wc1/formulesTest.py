import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_check():
    """geen van de functies print iets (moet returnen!)"""
    assert has_no_call_to(static.getSource(), "print")

@t.passed(no_syntax_error, hide=False)
@t.test()
def kwadraat():
    """kwadraat werkt correct"""
    assert defines_function("kwadraat")
    assert getFunction("kwadraat")(6) == 36
    assert getFunction("kwadraat")(-2) == 4

@t.passed(no_syntax_error, hide=False)
@t.test()
def derde_macht():
    """derde_macht werkt correct"""
    assert defines_function("derde_macht")
    assert getFunction("derde_macht")(1) == 1
    assert getFunction("derde_macht")(3) == 27

@t.passed(no_syntax_error, hide=False)
@t.test()
def avg3():
    """avg3 werkt correct"""
    assert defines_function("avg3")
    assert getFunction("avg3")(1,2,3) == 2
    assert getFunction("avg3")(1,1,1) == 1

@t.passed(no_syntax_error, hide=False)
@t.test()
def celsius_to_fahrenheit():
    """celsius_to_fahrenheit werkt correct"""
    assert defines_function("celsius_to_fahrenheit")
    assert getFunction("celsius_to_fahrenheit")(10) == 50
    assert getFunction("celsius_to_fahrenheit")(0) == 32
    assert getFunction("celsius_to_fahrenheit")(1) == 33.8

@t.passed(no_syntax_error, hide=False)
@t.test()
def fahrenheit_to_celsius():
    """fahrenheit_to_celsius werkt correct"""
    assert defines_function("fahrenheit_to_celsius")
    assert getFunction("fahrenheit_to_celsius")(50) == 10
    assert getFunction("fahrenheit_to_celsius")(32) == 0
    assert getFunction("fahrenheit_to_celsius")(33.8) == 1

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_leap_year():
    """is_leap_year werkt correct"""
    assert defines_function("is_leap_year")
    assert getFunction("is_leap_year")(1961) == False
    assert getFunction("is_leap_year")(1984) == True
    assert getFunction("is_leap_year")(1800) == False
    assert getFunction("is_leap_year")(1900) == False
    assert getFunction("is_leap_year")(2000) == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_valid_triangle():
    """is_valid_triangle werkt correct"""
    assert defines_function("is_valid_triangle")
    assert getFunction("is_valid_triangle")(3,4,5) == True
    assert getFunction("is_valid_triangle")(1,1,1) == True
    assert getFunction("is_valid_triangle")(1,0,1) == False
    assert getFunction("is_valid_triangle")(0,1,1) == False
    assert getFunction("is_valid_triangle")(1,1,0) == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_divisible():
    """is_divisible werkt correct"""
    assert defines_function("is_divisible")
    assert getFunction("is_divisible")(3,2) == False
    assert getFunction("is_divisible")(4,2) == True
    assert getFunction("is_divisible")(100,2) == True
    assert getFunction("is_divisible")(27,3) == True
    assert getFunction("is_divisible")(28,3) == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def solve_quadratic():
    """solve_quadratic werkt correct"""
    assert defines_function("solve_quadratic")
    assert getFunction("solve_quadratic")(1,-5,-14) in [(-2, 7), (7, -2)]
    assert getFunction("solve_quadratic")(1,15,50) in [(-5, -10), (-10, -5)]
    assert getFunction("solve_quadratic")(1,-2,-24) in [(6, -4), (-4, 6)]

@t.passed(no_syntax_error, hide=False)
@t.test()
def convert_seconds():
    """convert_seconds werkt correct"""
    assert defines_function("convert_seconds")
    assert getFunction("convert_seconds")(0) == (0, 0, 0)
    assert getFunction("convert_seconds")(1) == (0, 0, 1)
    assert getFunction("convert_seconds")(3600) == (1, 0, 0)
    assert getFunction("convert_seconds")(60) == (0, 1, 0)
    assert getFunction("convert_seconds")(65) == (0, 1, 5)
    assert getFunction("convert_seconds")(3661) == (1, 1, 1)

@t.passed(no_syntax_error, hide=False)
@t.test()
def max_of_three():
    """max_of_three werkt correct"""
    assert defines_function("max_of_three")
    assert getFunction("max_of_three")(1,1,1) == 1
    assert getFunction("max_of_three")(1,2,3) == 3
    assert getFunction("max_of_three")(1,3,2) == 3
    assert getFunction("max_of_three")(3,1,2) == 3
    assert getFunction("max_of_three")(3,2,1) == 3
    assert getFunction("max_of_three")(0,0,9) == 9

@t.passed(no_syntax_error, hide=False)
@t.test()
def grade_to_us():
    """grade_to_us werkt correct"""
    assert defines_function("grade_to_us")
    assert getFunction("grade_to_us")(8.5) == 'A+'
    assert getFunction("grade_to_us")(8.4) == 'A'
    assert getFunction("grade_to_us")(7.4) == 'B+'
    assert getFunction("grade_to_us")(6.6) == 'B'
    assert getFunction("grade_to_us")(6.1) == 'C'
    assert getFunction("grade_to_us")(5.9) == 'D'
    assert getFunction("grade_to_us")(1) == 'F'
