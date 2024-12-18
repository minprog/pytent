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
    potential_names = ['vowel_balance', 'vowel_balace']
    selected_function = None
    for name in potential_names:
        if defines_function_no_assert(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    src = extract_function_by_name(selected_function)
    assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert_doctest(selected_function, "aeiou", True)  # Alleen klinkers
    assert_doctest(selected_function, "bcdfg", False)  # Alleen medeklinkers
    assert_doctest(selected_function, "aeioubcdfg", False)  # Gelijke klinkers en medeklinkers
    assert_doctest(selected_function, "Thiiiiis iiiis a teeeeest sentence.", True)  # Meer klinkers
    assert_doctest(selected_function, "Ths s n mst knspnt.", False)  # Geen klinkers

@t.passed(no_syntax_error, hide=False)
@t.test()
def validate_house_address():
    """validate_house_address werkt correct"""
    potential_names = ['validate_house_address', 'validate_house_adress', 'validate_house_adres', 'valid_house_address']
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
    potential_names = ['humanize_string', 'hummanize_string']
    selected_function = None
    for name in potential_names:
        if defines_function_no_assert(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    src = extract_function_by_name(selected_function)
    assert no_string_methods_or_slicing(src)
    assert_doctest(selected_function, "employee_salary", "Employee Salary")
    assert_doctest(selected_function, "python_programming_language", "Python Programming Language")
    assert_doctest(selected_function, "test", "Test")
    assert_doctest(selected_function, "a_b_c_d", "A B C D")
    # assert_doctest('humanize_string', "", "")

@t.passed(no_syntax_error, hide=False)
@t.test()
def extract_even_number():
    """extract_even_number werkt correct"""
    potential_names = ['extract_even_number', 'extract_even_numbers']
    selected_function = None
    for name in potential_names:
        if defines_function_no_assert(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    src = extract_function_by_name(selected_function)
    assert no_string_methods_or_slicing(src)
    assert_doctest(selected_function, "abc1234def", 1234)
    assert_doctest(selected_function, "5678xyz", 5678)
    assert_doctest(selected_function, "ja123", 0)  # Geen even getallen
    assert_doctest(selected_function, "123 246", 246)  # Eerste even getal
    assert_doctest(selected_function, "222 246", 222)  # Eerste even getal

@t.passed(no_syntax_error, hide=False)
@t.test()
def average_sentence_length():
    """average_sentence_length werkt correct"""
    potential_names = ['avarage_sentence_length', 'average_sentence_length', 'avarage_sentence_legth', 'average_scentence_length', 'avarge_sentence_length', 'average_sentence_lenght']
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
