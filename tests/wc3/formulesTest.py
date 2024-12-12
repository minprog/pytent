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
def count_occurrences():
    """count_occurrences werkt correct"""
    assert_doctest('count_occurrences', ("hello", "l"), 2)
    assert_doctest('count_occurrences', ("hello", "e"), 1)
    assert_doctest('count_occurrences', ("hello", "x"), 0)

@t.passed(no_syntax_error, hide=False)
@t.test()
def has_O():
    """has_O werkt correct"""
    assert_doctest('has_O', "HELLO", True)
    assert_doctest('has_O', "hello", False)
    assert_doctest('has_O', "Ooops", True)

@t.passed(no_syntax_error, hide=False)
@t.test()
def find():
    """find werkt correct"""
    assert_doctest('find', ("hello", "e"), 1)
    assert_doctest('find', ("hello", "x"), -1)
    assert_doctest('find', ("hello", "l"), 2)

@t.passed(no_syntax_error, hide=False)
@t.test()
def has_up_and_down():
    """has_up_and_down werkt correct"""
    assert_doctest('has_up_and_down', "Hello", True)
    assert_doctest('has_up_and_down', "HELLO", False)
    assert_doctest('has_up_and_down', "hello", False)

@t.passed(no_syntax_error, hide=False)
@t.test()
def multiply():
    """multiply werkt correct"""
    assert_doctest('multiply', ("abc", 3), "abcabcabc")
    assert_doctest('multiply', ("x", 0), "")
    assert_doctest('multiply', ("", 5), "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def reverse_string():
    """reverse_string werkt correct"""
    assert_doctest('reverse_string', ("abcdef"), "fedcba")
    assert_doctest('reverse_string', (""), "")
    assert_doctest('reverse_string', ("a"), "a")

@t.passed(no_syntax_error, hide=False)
@t.test()
def leetspeak():
    """leetspeak werkt correct"""
    assert_doctest('leetspeak', "aleot", "41307")
    assert_doctest('leetspeak', "ALEOT", "41307")
    assert_doctest('leetspeak', "hello", "h3110")

@t.passed(no_syntax_error, hide=False)
@t.test()
def replace_char():
    """replace_char werkt correct"""
    assert_doctest('replace_char', ("hello", "l", "x"), "hexxo")
    assert_doctest('replace_char', ("hello", "e", "a"), "hallo")
    assert_doctest('replace_char', ("hello", "z", "x"), "hello")

@t.passed(no_syntax_error, hide=False)
@t.test()
def to_lower():
    """to_lower werkt correct"""
    assert_doctest('to_lower', "HeLLo", "hello")
    assert_doctest('to_lower', "HELLO", "hello")
    assert_doctest('to_lower', "hello", "hello")

@t.passed(no_syntax_error, hide=False)
@t.test()
def lstrip():
    """lstrip werkt correct"""
    assert_doctest('lstrip', '   hello', 'hello')
    assert_doctest('lstrip', 'hello   ', 'hello   ')
    assert_doctest('lstrip', '   hello   ', 'hello   ')
    assert_doctest('lstrip', '', '')

@t.passed(no_syntax_error, hide=False)
@t.test()
def rstrip():
    """rstrip werkt correct"""
    assert_doctest('rstrip', "hello   ", "hello")
    assert_doctest('rstrip', "hello world   ", "hello world")
    assert_doctest('rstrip', "   hello   ", "   hello")
    assert_doctest('rstrip', '', '')

@t.passed(no_syntax_error, hide=False)
@t.test()
def split_in_two():
    """split_in_two werkt correct"""
    assert_doctest('split_in_two', ("joey:22", ":"), ("joey", "22"))
    assert_doctest('split_in_two', ("hello:world", ":"), ("hello", "world"))
    assert_doctest('split_in_two', ("a:b", ":"), ("a", "b"))
