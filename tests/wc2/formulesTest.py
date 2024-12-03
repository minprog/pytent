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
    assert defines_function("print_collatz")
    f = getFunction("print_collatz")
    f(8)
    assert f.printOutput.strip() == "8\n4\n2\n1".strip()
    f(12)
    assert f.printOutput.strip() == "12\n6\n3\n10\n5\n16\n8\n4\n2\n1".strip()

@t.passed(no_syntax_error, hide=False)
@t.test()
def collatz_length():
    """collatz_length werkt correct"""
    assert defines_function("collatz_length")
    assert getFunction("collatz_length")(8) == 4
    assert getFunction("collatz_length")(12) == 10
    assert getFunction("collatz_length")(1) == 1

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_prime():
    """is_prime werkt correct"""
    assert defines_function("is_prime")
    assert getFunction("is_prime")(2) == True
    assert getFunction("is_prime")(3) == True
    assert getFunction("is_prime")(4) == False
    assert getFunction("is_prime")(5) == True
    assert getFunction("is_prime")(6) == False
    assert getFunction("is_prime")(7) == True
    assert getFunction("is_prime")(8) == False
    assert getFunction("is_prime")(9) == False
    assert getFunction("is_prime")(10) == False
    assert getFunction("is_prime")(11) == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_primes_until():
    """print_primes_until werkt correct (print 1 getal per regel)"""
    assert defines_function("print_primes_until")
    f = getFunction("print_primes_until")
    f(2)
    assert f.printOutput.strip() == "2".strip(), "print_primes_until(2)"
    f(3)
    assert f.printOutput.strip() == "2\n3".strip(), "print_primes_until(3)"
    f(4)
    assert f.printOutput.strip() == "2\n3".strip(), "print_primes_until(4)"
    f(5)
    assert f.printOutput.strip() == "2\n3\n5".strip(), "print_primes_until(5)"
    f(6)
    assert f.printOutput.strip() == "2\n3\n5".strip(), "print_primes_until(6)"
    f(7)
    assert f.printOutput.strip() == "2\n3\n5\n7".strip(), "print_primes_until(7)"
    f(8)
    assert f.printOutput.strip() == "2\n3\n5\n7".strip(), "print_primes_until(8)"
    f(9)
    assert f.printOutput.strip() == "2\n3\n5\n7".strip(), "print_primes_until(9)"
    f(10)
    assert f.printOutput.strip() == "2\n3\n5\n7".strip(), "print_primes_until(10)"

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_n_primes():
    """print_n_primes werkt correct (print 1 getal per regel)"""
    assert defines_function("print_n_primes")
    f = getFunction("print_n_primes")
    f(0)
    assert f.printOutput.strip() == "".strip(), "print_n_primes(0)"
    f(1)
    assert f.printOutput.strip() == "2".strip(), "print_n_primes(1)"
    f(2)
    assert f.printOutput.strip() == "2\n3".strip(), "print_n_primes(2)"
    f(3)
    assert f.printOutput.strip() == "2\n3\n5".strip(), "print_n_primes(3)"

@t.passed(no_syntax_error, hide=False)
@t.test()
def print_nth_prime():
    """print_nth_prime werkt correct"""
    assert defines_function("print_nth_prime")
    f = getFunction("print_nth_prime")
    f(1)
    assert f.printOutput.strip() == "2".strip(), "print_nth_prime(1)"
    f(2)
    assert f.printOutput.strip() == "3".strip(), "print_nth_prime(2)"
    f(3)
    assert f.printOutput.strip() == "5".strip(), "print_nth_prime(3)"
    f(4)
    assert f.printOutput.strip() == "7".strip(), "print_nth_prime(4)"
    f(1000)
    assert f.printOutput.strip() == "7919".strip(), "print_nth_prime(1000)"

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_leap_years():
    """count_leap_years werkt correct"""
    assert defines_function("count_leap_years")
    assert getFunction("count_leap_years")(2000, 2001) == 1
    assert getFunction("count_leap_years")(1800, 1900) == 24

@t.passed(no_syntax_error, hide=False)
@t.test()
def nth_leap_year():
    """nth_leap_year werkt correct"""
    assert defines_function("nth_leap_year")
    assert getFunction("nth_leap_year")(2000, 1) == 2000
    assert getFunction("nth_leap_year")(2000, 2) == 2004
