from checkpy import *

from _remove_main import *
from _forbidden_basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def switch_case():
    """switch_case werkt correct"""
    assert defines_function("switch_case")
    assert getFunction("switch_case")("Hello, world!") == 'hELLO, WORLD!'
    assert getFunction("switch_case")("run") == 'RUN'
    assert getFunction("switch_case")("@") == '@'

@t.passed(no_syntax_error, hide=False)
@t.test()
def time_to_24_hours():
    """time_to_24_hours werkt correct"""
    assert defines_function("time_to_24_hours")
    assert getFunction("time_to_24_hours")('11:32 AM') == '11:32'
    assert getFunction("time_to_24_hours")('10:45 AM') == '10:45'
    assert getFunction("time_to_24_hours")('12:32 AM') == '0:32'
    assert getFunction("time_to_24_hours")('9:32 PM') == '21:32'
    assert getFunction("time_to_24_hours")('10:45 PM') == '22:45'

@t.passed(no_syntax_error, hide=False)
@t.test()
def remove_numbers():
    """remove_numbers werkt correct"""
    assert defines_function("remove_numbers")
    assert getFunction("remove_numbers")(['1. these', '2. stories', '3. wear', '4. scars', '5. stretchmarks', '6. wrinkles']) == ['these', 'stories', 'wear', 'scars', 'stretchmarks', 'wrinkles']
    assert getFunction("remove_numbers")(['8. these', '9. stories', '1. wear', '2. scars', '3. stretchmarks', '4. wrinkles']) == ['these', 'stories', 'wear', 'scars', 'stretchmarks', 'wrinkles']

@t.passed(no_syntax_error, hide=False)
@t.test()
def rotations():
    """rotations werkt correct"""
    assert defines_function("rotations")
    assert getFunction("rotations")("happy!") == ['happy!', 'appy!h', 'ppy!ha', 'py!hap', 'y!happ', '!happy']
    assert getFunction("rotations")("app") == ['app', 'ppa', 'pap']
