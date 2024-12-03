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
def stretch():
    """stretch werkt correct"""
    assert defines_function("stretch")
    assert getFunction("stretch")("abc") == "abbccc"
    assert getFunction("stretch")("Hoi!") == "Hooiii!!!!"
    assert getFunction("stretch")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def autocorrect():
    """autocorrect werkt correct"""
    assert defines_function("autocorrect")
    assert getFunction("autocorrect")("Dit hier,, dit kan niet.") == "Dit hier, dit kan niet."
    assert getFunction("autocorrect")("?!...!!") == "?!.!", "meerdere verschillende combinaties leestekens achter elkaar"
    assert getFunction("autocorrect")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def str_diff():
    """str_diff werkt correct"""
    assert defines_function("str_diff")
    assert getFunction("str_diff")("muikku", "kinkku") == 3
    assert getFunction("str_diff")("aa", "aabb") == 2
    assert getFunction("str_diff")("ab", "cdab") == 4

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_valid_email():
    """is_valid_email werkt correct"""
    assert defines_function("is_valid_email")
    assert getFunction("is_valid_email")("test@example.com") == True
    assert getFunction("is_valid_email")("invalid-email") == False
    assert getFunction("is_valid_email")("test@.com") == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def longest_word_length():
    """longest_word_length werkt correct"""
    assert defines_function("longest_word_length")
    assert getFunction("longest_word_length")("lahetetty joensuun hotellista") == 10
    assert getFunction("longest_word_length")("abc def") == 3
    assert getFunction("longest_word_length")("") == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def encrypt():
    """encrypt werkt correct"""
    assert defines_function("encrypt")
    assert getFunction("encrypt")("abc") == "zyx"
    assert getFunction("encrypt")("xyz") == "cba"
    assert getFunction("encrypt")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_nth_word():
    """remove_nth_word werkt correct"""
    assert defines_function("remove_nth_word")
    assert getFunction("remove_nth_word")("abc def geh", 3) in ["abc def", "abc def "]
    assert getFunction("remove_nth_word")("one two three four", 2) in ["one three four", "one  three four"]
    assert getFunction("remove_nth_word")("single", 1) in ["", " "]

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_character():
    """remove_character werkt correct"""
    assert defines_function("remove_character")
    assert getFunction("remove_character")("hello", "l") == "heo"
    assert getFunction("remove_character")("banana", "a") == "bnn"
    assert getFunction("remove_character")("", "x") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def find_longest_word():
    """find_longest_word werkt correct"""
    assert defines_function("find_longest_word")
    assert getFunction("find_longest_word")("abc def gehijk lmn") == "gehijk"
    assert getFunction("find_longest_word")("one two three") == "three"
    assert getFunction("find_longest_word")("") == ""

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_substring():
    """count_substring werkt correct"""
    assert defines_function("count_substring")
    assert getFunction("count_substring")("banana", "na") == 2
    assert getFunction("count_substring")("aaaa", "aa") == 3
    assert getFunction("count_substring")("hello", "x") == 0
