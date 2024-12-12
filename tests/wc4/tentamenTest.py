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
    assert_doctest('stretch', "abc", "abbccc")
    assert_doctest('stretch', "Hoi!", "Hooiii!!!!")
    assert_doctest('stretch', "", "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def autocorrect():
    """autocorrect werkt correct"""
    assert_doctest('autocorrect', "Dit hier,, dit kan niet.", "Dit hier, dit kan niet.")
    assert_doctest('autocorrect', "?!...!!", "?!.!", hint="meerdere verschillende combinaties leestekens achter elkaar")
    assert_doctest('autocorrect', "", "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def str_diff():
    """str_diff werkt correct"""
    assert_doctest('str_diff', ("muikku", "kinkku"), 3)
    assert_doctest('str_diff', ("aa", "aabb"), 2)
    assert_doctest('str_diff', ("ab", "cdab"), 4)

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_valid_email():
    """is_valid_email werkt correct"""
    assert_doctest('is_valid_email', "test@example.com", True)
    assert_doctest('is_valid_email', "invalid-email", False)
    assert_doctest('is_valid_email', "test@.com", False)

@t.passed(no_syntax_error, hide=False)
@t.test()
def longest_word_length():
    """longest_word_length werkt correct"""
    assert_doctest('longest_word_length', "lahetetty joensuun hotellista", 10)
    assert_doctest('longest_word_length', "abc def", 3)
    assert_doctest('longest_word_length', "", 0)

@t.passed(no_syntax_error, hide=False)
@t.test()
def encrypt():
    """encrypt werkt correct"""
    assert_doctest('encrypt', "abc", "zyx")
    assert_doctest('encrypt', "xyz", "cba")
    assert_doctest('encrypt', "", "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_nth_word():
    """remove_nth_word werkt correct"""
    assert_doctest('remove_nth_word', ("abc def geh", 3), "abc def ")
    assert_doctest('remove_nth_word', ("one two three four", 2), "one  three four")
    assert_doctest('remove_nth_word', ("single", 1), "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_character():
    """remove_character werkt correct"""
    assert_doctest('remove_character', ("hello", "l"), "heo")
    assert_doctest('remove_character', ("banana", "a"), "bnn")
    assert_doctest('remove_character', ("", "x"), "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def find_longest_word():
    """find_longest_word werkt correct"""
    assert_doctest('find_longest_word', ("abc def gehijk lmn"), "gehijk")
    assert_doctest('find_longest_word', ("one two three"), "three")
    assert_doctest('find_longest_word', (""), "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_substring():
    """count_substring werkt correct"""
    assert_doctest('count_substring', ("banana", "na"), 2)
    assert_doctest('count_substring', ("aaaa", "aa"), 3)
    assert_doctest('count_substring', ("hello", "x"), 0)
