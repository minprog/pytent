from checkpy import *
from _basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def has_digits_but_no_spaces():
    """has_digits_but_no_spaces werkt correct"""
    assert assert_defines_function("has_digits_but_no_spaces")
    src = extract_function_by_name("has_digits_but_no_spaces")
    assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert has_no_call_to(src, 'min'), "Bevat geen aanroep naar min()"
    assert has_no_call_to(src, 'max'), "Bevat geen aanroep naar max()"
    assert has_no_call_to(src, 'reversed'), "Bevat geen aanroep naar reversed()"
    assert getFunction("has_digits_but_no_spaces")("hello123") == True
    assert getFunction("has_digits_but_no_spaces")("_hello 123") == False
    assert getFunction("has_digits_but_no_spaces")("_hello123") == True
    assert getFunction("has_digits_but_no_spaces")("hello3") == True
    assert getFunction("has_digits_but_no_spaces")("hello3a") == True
    assert getFunction("has_digits_but_no_spaces")(" hello3") == False
    assert getFunction("has_digits_but_no_spaces")(" hello3a") == False
    assert getFunction("has_digits_but_no_spaces")("1hello ") == False
    assert getFunction("has_digits_but_no_spaces")("1hello") == True
    assert getFunction("has_digits_but_no_spaces")("no_digits") == False
    assert getFunction("has_digits_but_no_spaces")("no_spaces1") == True

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_valid_plate():
    """is_valid_plate werkt correct"""
    assert assert_defines_function("is_valid_plate")
    src = extract_function_by_name("is_valid_plate")
    assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert has_no_call_to(src, 'min'), "Bevat geen aanroep naar min()"
    assert has_no_call_to(src, 'max'), "Bevat geen aanroep naar max()"
    assert has_no_call_to(src, 'reversed'), "Bevat geen aanroep naar reversed()"
    assert getFunction("is_valid_plate")("A-123-BC") == True
    assert getFunction("is_valid_plate")("1-HALLO-45") == True
    assert getFunction("is_valid_plate")("123-AB1-C") == False
    assert getFunction("is_valid_plate")("A23-1-C") == False
    assert getFunction("is_valid_plate")("AB-1-C") == True
    assert getFunction("is_valid_plate")("AB-1-C3") == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def avg_vowels_per_word():
    """avg_vowels_per_word werkt correct"""
    assert assert_defines_function("avg_vowels_per_word")
    src = extract_function_by_name("avg_vowels_per_word")
    # assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert has_no_call_to(src, 'min'), "Bevat geen aanroep naar min()"
    assert has_no_call_to(src, 'max'), "Bevat geen aanroep naar max()"
    assert has_no_call_to(src, 'reversed'), "Bevat geen aanroep naar reversed()"
    assert getFunction("avg_vowels_per_word")("dit is een test") == 1.25
    assert getFunction("avg_vowels_per_word")("alleen  klinkers") == 2.5
    assert getFunction("avg_vowels_per_word")("geen    klinkers hier") == 2
    assert getFunction("avg_vowels_per_word")("dit") == 1.0

@t.passed(no_syntax_error, hide=False)
@t.test()
def is_num_palindrome():
    """is_num_palindrome werkt correct"""
    assert assert_defines_function("is_num_palindrome")
    src = extract_function_by_name("is_num_palindrome")
    # assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert has_no_call_to(src, 'min'), "Bevat geen aanroep naar min()"
    assert has_no_call_to(src, 'max'), "Bevat geen aanroep naar max()"
    assert has_no_call_to(src, 'reversed'), "Bevat geen aanroep naar reversed()"
    assert getFunction("is_num_palindrome")("12321") == True
    assert getFunction("is_num_palindrome")("1") == True
    assert getFunction("is_num_palindrome")("123") == False
    assert getFunction("is_num_palindrome")("543212345") == True
    assert getFunction("is_num_palindrome")("5432a2345") == False

@t.passed(no_syntax_error, hide=False)
@t.test()
def titlecase():
    """titlecase werkt correct"""
    potential_names = ['titlecase', 'titelcase', 'title_case']
    selected_function = None
    for name in potential_names:
        if defines_function(name):
            selected_function = name
            break
    if selected_function == None: raise AssertionError(f"{' of '.join(potential_names)} niet gevonden")
    # assert defines_function("titlecase")
    src = extract_function_by_name(selected_function)
    # assert no_string_methods_or_slicing(src)
    assert has_no_call_to(src, 'sorted'), "Bevat geen aanroep naar sorted()"
    assert has_no_call_to(src, 'min'), "Bevat geen aanroep naar min()"
    assert has_no_call_to(src, 'max'), "Bevat geen aanroep naar max()"
    assert has_no_call_to(src, 'reversed'), "Bevat geen aanroep naar reversed()"
    assert getFunction(selected_function)("dit is een test") == 'Dit Is Een Test'
    assert getFunction(selected_function)("dit is een testd") == 'Dit Is Een Testd'
    assert getFunction(selected_function)("hallo wereld") == 'Hallo Wereld'
    assert getFunction(selected_function)("python PROGRAMMEER les") == 'Python Programmeer Les'
