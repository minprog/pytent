import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

from checkpy import *

from _remove_main import *
from _basics import *
from _static_analysis import *

from checkpy import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def check_forbidden():
    """check of geen geavanceerde python gebruikt"""
    assert in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@t.passed(no_syntax_error, hide=False)
@t.test()
def same_first_last():
    """same_first_last werkt correct"""
    assert defines_function("same_first_last")
    assert getFunction("same_first_last")([1, 2, 3, 1]) == True
    assert getFunction("same_first_last")([1, 2, 3]) == False
    assert getFunction("same_first_last")([]) == False, "same_first_last([]) moet ook een [] teruggeven"

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_longer():
    """is_longer werkt correct"""
    assert defines_function("is_longer")
    assert getFunction("is_longer")([1, 2, 3], [1, 2]) == True
    assert getFunction("is_longer")([], [1]) == False
    assert getFunction("is_longer")([], []) == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_palindromish():
    """is_palindromish werkt correct"""
    assert defines_function("is_palindromish")
    assert getFunction("is_palindromish")([1, 2, 3, 2, 1]) == True
    assert getFunction("is_palindromish")([1, 2, 3]) == False
    assert getFunction("is_palindromish")([]) == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_palindromish_eff():
    """is_palindromish_eff werkt correct"""
    assert defines_function("is_palindromish_eff")
    assert getFunction("is_palindromish_eff")([1, 2, 3, 2, 1]) == True
    assert getFunction("is_palindromish_eff")([1, 2, 3]) == False
    assert getFunction("is_palindromish_eff")([]) == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def filter_even():
    """filter_even werkt correct"""
    assert defines_function("filter_even")
    assert getFunction("filter_even")([1, 2, 3, 4]) == [2, 4]
    assert getFunction("filter_even")([1, 3, 5]) == []
    assert getFunction("filter_even")([]) == []

@t.passed(no_syntax_error, hide=False)
@t.test()
def all_even():
    """all_even werkt correct"""
    assert defines_function("all_even")
    assert getFunction("all_even")([2, 4, 6]) == True
    assert getFunction("all_even")([2, 4, 5]) == False
    assert getFunction("all_even")([]) == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def max_element():
    """max_element werkt correct"""
    assert defines_function("max_element")
    assert getFunction("max_element")([1, 2, 3]) == 3
    assert getFunction("max_element")([-1, -2, -3]) == -1
    assert getFunction("max_element")([42]) == 42

@t.passed(no_syntax_error, hide=False)
@t.test()
def element_exists():
    """element_exists werkt correct"""
    assert defines_function("element_exists")
    assert getFunction("element_exists")([1, 2, 3], 2) == True
    assert getFunction("element_exists")([1, 2, 3], 4) == False
    assert getFunction("element_exists")([], 1) == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_occurrences():
    """count_occurrences werkt correct"""
    assert defines_function("count_occurrences")
    assert getFunction("count_occurrences")([1, 2, 2, 3], 2) == 2
    assert getFunction("count_occurrences")([1, 2, 3], 4) == 0
    assert getFunction("count_occurrences")([], 1) == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_duplicates():
    """remove_duplicates werkt correct"""
    assert defines_function("remove_duplicates")
    assert getFunction("remove_duplicates")([1, 2, 2, 3]) == [1, 2, 3]
    assert getFunction("remove_duplicates")([1, 1, 1]) == [1]
    assert getFunction("remove_duplicates")([]) == []

@t.passed(no_syntax_error, hide=False)
@t.test()
def merge_sorted_lists():
    """merge_sorted_lists werkt correct"""
    assert defines_function("merge_sorted_lists")
    assert getFunction("merge_sorted_lists")([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert getFunction("merge_sorted_lists")([], [2, 4]) == [2, 4]
    assert getFunction("merge_sorted_lists")([], []) == []
