from checkpy import *

from _remove_main import *
from _forbidden_basics import *
from _static_analysis import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def dubbele_hoofdletters():
    """dubbele_hoofdletters werkt correct"""
    assert defines_function("dubbele_hoofdletters")
    assert getFunction("dubbele_hoofdletters")("Wat een GEKKE Tekst") == 'WaT EeN GekkE TeksT'

@t.passed(no_syntax_error, hide=False)
@t.test()
def filter_gemiddelde():
    """filter_gemiddelde werkt correct"""
    assert defines_function("filter_gemiddelde")
    assert getFunction("filter_gemiddelde")(10.5, [[1, 6, 9], [12], [10, 10], [10, 11, 11]]) == [[12], [10, 11, 11]]

@t.passed(no_syntax_error, hide=False)
@t.test()
def split_lengte():
    """split_lengte werkt correct"""
    assert defines_function("split_lengte")
    assert getFunction("split_lengte")(5, ['these', 'stories', 'we', 'wear', 'scars', 'stretchmarks', 'wrinkles']) == (['these', 'stories', 'scars', 'stretchmarks', 'wrinkles'], ['we', 'wear'])

@t.passed(no_syntax_error, hide=False)
@t.test()
def converteer_naar_lijst():
    """converteer_naar_lijst werkt correct"""
    assert defines_function("converteer_naar_lijst")
    assert getFunction("converteer_naar_lijst")("1,2,3") == [1, 2, 3]

@t.passed(no_syntax_error, hide=False)
@t.test()
def voortschrijdende_som():
    """voortschrijdende_som werkt correct"""
    assert defines_function("voortschrijdende_som")
    assert getFunction("voortschrijdende_som")("1,2,3") == [6]
    assert getFunction("voortschrijdende_som")("1,2,3,4,5,6,7") == [6, 9, 12, 15, 18]
