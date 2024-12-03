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
    assert defines_function("count_occurrences")
    assert getFunction("count_occurrences")("hello", "l") == 2
    assert getFunction("count_occurrences")("hello", "e") == 1
    assert getFunction("count_occurrences")("hello", "x") == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def has_O():
    """has_O werkt correct"""
    assert defines_function("has_O")
    assert getFunction("has_O")("HELLO") == True
    assert getFunction("has_O")("hello") == False
    assert getFunction("has_O")("Ooops") == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def find():
    """find werkt correct"""
    assert defines_function("find")
    assert getFunction("find")("hello", "e") == 1
    assert getFunction("find")("hello", "x") == -1
    assert getFunction("find")("hello", "l") == 2

@t.passed(no_syntax_error, hide=False)
@t.test()
def has_up_and_down():
    """has_up_and_down werkt correct"""
    assert defines_function("has_up_and_down")
    assert getFunction("has_up_and_down")("Hello") == True
    assert getFunction("has_up_and_down")("HELLO") == False
    assert getFunction("has_up_and_down")("hello") == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def multiply():
    """multiply werkt correct"""
    assert defines_function("multiply")
    assert getFunction("multiply")("abc", 3) == "abcabcabc"
    assert getFunction("multiply")("x", 0) == ""
    assert getFunction("multiply")("", 5) == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def reverse_string():
    """reverse_string werkt correct"""
    assert defines_function("reverse_string")
    assert getFunction("reverse_string")("abcdef") == "fedcba"
    assert getFunction("reverse_string")("") == ""
    assert getFunction("reverse_string")("a") == "a"

@t.passed(no_syntax_error, hide=False)
@t.test()
def leetspeak():
    """leetspeak werkt correct"""
    assert defines_function("leetspeak")
    assert getFunction("leetspeak")("aleot") == "41307"
    assert getFunction("leetspeak")("ALEOT") == "41307"
    assert getFunction("leetspeak")("hello") == "h3110"

@t.passed(no_syntax_error, hide=False)
@t.test()
def replace_char():
    """replace_char werkt correct"""
    assert defines_function("replace_char")
    assert getFunction("replace_char")("hello", "l", "x") == "hexxo"
    assert getFunction("replace_char")("hello", "e", "a") == "hallo"
    assert getFunction("replace_char")("hello", "z", "x") == "hello"

@t.passed(no_syntax_error, hide=False)
@t.test()
def to_lower():
    """to_lower werkt correct"""
    assert defines_function("to_lower")
    assert getFunction("to_lower")("HeLLo") == "hello"
    assert getFunction("to_lower")("HELLO") == "hello"
    assert getFunction("to_lower")("hello") == "hello"

@t.passed(no_syntax_error, hide=False)
@t.test()
def lstrip():
    """lstrip werkt correct"""
    assert defines_function("lstrip")
    assert getFunction("lstrip")("   hello") == "hello"
    assert getFunction("lstrip")("hello   ") == "hello   "
    assert getFunction("lstrip")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def rstrip():
    """rstrip werkt correct"""
    assert defines_function("rstrip")
    assert getFunction("rstrip")("hello world   ") == "hello world"
    # assert getFunction("rstrip")("   hello   ") == "   hello"
    assert getFunction("rstrip")("hello   ") == "hello"
    assert getFunction("rstrip")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def split_in_two():
    """split_in_two werkt correct"""
    assert defines_function("split_in_two")
    assert getFunction("split_in_two")("joey:22", ":") == ("joey", "22")
    assert getFunction("split_in_two")("hello:world", ":") == ("hello", "world")
    assert getFunction("split_in_two")("a:b", ":") == ("a", "b")
