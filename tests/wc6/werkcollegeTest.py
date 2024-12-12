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
def count():
    """count werkt correct"""
    assert defines_function("count")
    assert getFunction("count")([1, 2, 3, 2]) == {1: 1, 2: 2, 3: 1}
    assert getFunction("count")([4, 4, 4]) == {4: 3}
    assert getFunction("count")([]) == {}

@t.passed(no_syntax_error, hide=False)
@t.test()
def list_duplicates():
    """list_duplicates werkt correct"""
    assert defines_function("list_duplicates")
    assert getFunction("list_duplicates")([1, 2, 3, 2, 3, 3]) == {2, 3}
    assert getFunction("list_duplicates")([1, 2, 3]) == set()
    assert getFunction("list_duplicates")([]) == set()

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_values():
    """get_values werkt correct"""
    assert defines_function("get_values")
    assert getFunction("get_values")({"a": 1, "b": 2, "c": 3}) == [1, 2, 3]
    assert getFunction("get_values")({}) == []
    assert getFunction("get_values")({"x": 42}) == [42]

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_normal():
    """is_normal werkt correct"""
    assert defines_function("is_normal")
    assert getFunction("is_normal")({"a": 0.5, "b": 0.5}) == True
    assert getFunction("is_normal")({"a": 0.3, "b": 0.7, "c": 0.1}) == False
    assert getFunction("is_normal")({}) == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def count_values():
    """count_values werkt correct"""
    assert defines_function("count_values")
    assert getFunction("count_values")({"a": 1, "b": 2, "c": 1}) == 2
    assert getFunction("count_values")({"a": 1, "b": 2, "c": 3}) == 3
    assert getFunction("count_values")({}) == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def reverse_dict():
    """reverse_dict werkt correct"""
    assert defines_function("reverse_dict")
    assert getFunction("reverse_dict")({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert getFunction("reverse_dict")({}) == {}
    assert getFunction("reverse_dict")({"x": 42}) == {42: "x"}

@t.passed(no_syntax_error, hide=False)
@t.test()
def minst_voorkomende():
    """minst_voorkomende werkt correct"""
    assert_doctest('minst_voorkomende', {"pepernoten": 100, "taaitaai": 20, "kruidnoten": 501}, "taaitaai")
    assert_doctest('minst_voorkomende', {"a": 1, "b": 1, "c": 2}, "a")
    assert_doctest('minst_voorkomende', {"x": 10}, "x")

@t.passed(no_syntax_error, hide=False)
@t.test()
def tel_dubbele():
    """tel_dubbele werkt correct"""
    assert defines_function("tel_dubbele")
    assert getFunction("tel_dubbele")({"a": 1, "b": 2, "c": 1}) == 1
    assert getFunction("tel_dubbele")({"a": 1, "b": 2, "c": 3}) == 0
    assert getFunction("tel_dubbele")({}) == 0

@t.passed(no_syntax_error, hide=False)
@t.test()
def dict_intersect():
    """dict_intersect werkt correct"""
    assert defines_function("dict_intersect")
    assert getFunction("dict_intersect")({"a": 1, "b": 2}, {"a": 1, "c": 3}) == {"a": 1}
    assert getFunction("dict_intersect")({"x": 42}, {"y": 42}) == {}
    assert getFunction("dict_intersect")({}, {}) == {}

@t.passed(no_syntax_error, hide=False)
@t.test()
def get_valuable_letters():
    """get_valuable_letters werkt correct"""
    assert_doctest('get_valuable_letters', 4, ["c", "f", "h", "j", "q", "u", "v", "w", "x", "y", "z"])
    assert_doctest('get_valuable_letters', 8, ["q", "x", "y"])
    assert_doctest('get_valuable_letters', 11, [])
