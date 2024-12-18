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
def vowel_balance():
    """vowel_balance werkt correct"""
    assert defines_function("vowel_balance")
    src = extract_function_by_name("vowel_balance")
    assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert_doctest('vowel_balance', "aeiou", True)  # Alleen klinkers
    assert_doctest('vowel_balance', "bcdfg", False)  # Alleen medeklinkers
    assert_doctest('vowel_balance', "aeioubcdfg", False)  # Gelijke klinkers en medeklinkers
    assert_doctest('vowel_balance', "Thiiiiis iiiis a teeeeest sentence.", True)  # Meer klinkers
    assert_doctest('vowel_balance', "Ths s n mst knspnt.", False)  # Geen klinkers

@t.passed(no_syntax_error, hide=False)
@t.test()
def validate_house_address():
    """validate_house_address werkt correct"""
    potential_names = ['validate_house_address', 'validate_house_adress']
    selected_function = None
    for name in potential_names:
        if defines_function_no_assert(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    src = extract_function_by_name(selected_function)
    assert no_string_methods_or_slicing(src)
    assert_doctest(selected_function, "Mainstreet 123", True)
    assert_doctest(selected_function, "Avenue 45", True)
    assert_doctest(selected_function, "mainstreet 123", False)  # Geen hoofdletter aan het begin
    assert_doctest(selected_function, "MainStreet 123", False)  # Meer dan één hoofdletter
    assert_doctest(selected_function, "Mainstreet 123B", False)  # Alfabetische tekens na cijfers
    assert_doctest(selected_function, "Mainstreet", False)  # Geen cijfers
    assert_doctest(selected_function, "123 Mainstreet", False)  # Cijfers eerst

@t.passed(no_syntax_error, hide=False)
@t.test()
def humanize_string():
    """humanize_string werkt correct"""
    assert defines_function("humanize_string")
    src = extract_function_by_name("humanize_string")
    assert no_string_methods_or_slicing(src)
    assert_doctest('humanize_string', "employee_salary", "Employee Salary")
    assert_doctest('humanize_string', "python_programming_language", "Python Programming Language")
    assert_doctest('humanize_string', "test", "Test")
    assert_doctest('humanize_string', "a_b_c_d", "A B C D")
    # assert_doctest('humanize_string', "", "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def extract_even_number():
    """extract_even_number werkt correct"""
    assert defines_function("extract_even_number")
    src = extract_function_by_name("extract_even_number")
    assert no_string_methods_or_slicing(src)
    assert_doctest('extract_even_number', "abc1234def", 1234)
    assert_doctest('extract_even_number', "5678xyz", 5678)
    assert_doctest('extract_even_number', "ja123", 0)  # Geen even getallen
    assert_doctest('extract_even_number', "123 246", 246)  # Eerste even getal
    assert_doctest('extract_even_number', "222 246", 222)  # Eerste even getal

@t.passed(no_syntax_error, hide=False)
@t.test()
def average_sentence_length():
    """average_sentence_length werkt correct"""
    potential_names = ['avarage_sentence_length', 'average_sentence_length']
    selected_function = None
    for name in potential_names:
        if defines_function_no_assert(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    src = extract_function_by_name(selected_function)
    assert no_string_methods_or_slicing(src)
    assert_doctest(selected_function, "This is a test.", 4.0)
    assert_doctest(selected_function, "This is a test. And another.", 3.0)
    assert_doctest(selected_function, "This is a test. Bruh.", 2.5)
    assert_doctest(selected_function, "One sentence.", 2.0)
    assert_doctest(selected_function, "Word.", 1.0)
