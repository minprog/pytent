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
def check_forbidden():
    """check of geen geavanceerde python gebruikt"""
    assert in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    # assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_positive_int():
    """get_positive_int is aanwezig"""
    assert defines_function("get_positive_int")

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_any_int_but_0():
    """get_any_int_but_0 is aanwezig"""
    assert defines_function("get_any_int_but_0")

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_min_int():
    """get_min_int is aanwezig"""
    assert defines_function("get_min_int")

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_two_ints_in_order():
    """get_two_ints_in_order is aanwezig"""
    assert defines_function("get_two_ints_in_order")

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_collatz():
    """print_collatz werkt correct (print 1 getal per regel)"""
    assert_doctest('print_collatz', 8, "8\n4\n2\n1", use_output=True)
    assert_doctest('print_collatz', 12, "12\n6\n3\n10\n5\n16\n8\n4\n2\n1", use_output=True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def collatz_length():
    """collatz_length werkt correct"""
    assert_doctest('collatz_length', 8, 4)
    assert_doctest('collatz_length', 12, 10)
    assert_doctest('collatz_length', 1, 1)

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_prime():
    """is_prime werkt correct"""
    assert_doctest('is_prime', 2, True)
    assert_doctest('is_prime', 3, True)
    assert_doctest('is_prime', 4, False)
    assert_doctest('is_prime', 5, True)
    assert_doctest('is_prime', 6, False)
    assert_doctest('is_prime', 7, True)
    assert_doctest('is_prime', 8, False)
    assert_doctest('is_prime', 9, False)
    assert_doctest('is_prime', 10, False)
    assert_doctest('is_prime', 11, True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_primes_until():
    """print_primes_until werkt correct (print 1 getal per regel)"""
    assert_doctest('print_primes_until', 2, "2", use_output=True)
    assert_doctest('print_primes_until', 3, "2\n3", use_output=True)
    assert_doctest('print_primes_until', 4, "2\n3", use_output=True)
    assert_doctest('print_primes_until', 5, "2\n3\n5", use_output=True)
    assert_doctest('print_primes_until', 6, "2\n3\n5", use_output=True)
    assert_doctest('print_primes_until', 7, "2\n3\n5\n7", use_output=True)
    assert_doctest('print_primes_until', 8, "2\n3\n5\n7", use_output=True)
    assert_doctest('print_primes_until', 9, "2\n3\n5\n7", use_output=True)
    assert_doctest('print_primes_until', 10, "2\n3\n5\n7", use_output=True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_n_primes():
    """print_n_primes werkt correct (print 1 getal per regel)"""
    assert_doctest('print_n_primes', 0, "", use_output=True)
    assert_doctest('print_n_primes', 1, "2", use_output=True)
    assert_doctest('print_n_primes', 2, "2\n3", use_output=True)
    assert_doctest('print_n_primes', 3, "2\n3\n5", use_output=True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_nth_prime():
    """print_nth_prime werkt correct (geen return maar print!)"""
    assert_doctest('print_nth_prime', 1, "2", use_output=True)
    assert_doctest('print_nth_prime', 2, "3", use_output=True)
    assert_doctest('print_nth_prime', 3, "5", use_output=True)
    assert_doctest('print_nth_prime', 4, "7", use_output=True)
    assert_doctest('print_nth_prime', 1000, "7919", use_output=True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_leap_years():
    """count_leap_years werkt correct"""
    assert_doctest('count_leap_years', (2000, 2001), 1)
    assert_doctest('count_leap_years', (1800, 1900), 24)

@t.passed(no_syntax_error, hide=False)
@t.test()
def nth_leap_year():
    """nth_leap_year werkt correct"""
    assert_doctest('nth_leap_year', (2000, 1), 2000)
    assert_doctest('nth_leap_year', (2000, 2), 2004)
