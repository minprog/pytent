from checkpy import *
from _basics import *

@t.passed(no_syntax_error, hide=False)
@t.test()
def contact_list():
    """contactbeheer werkt correct zoals voorbeeld in opgave"""
    entries = []
    output  = []
    
    entries.append("add January Wilson +31600982184 jan@wilstore.com")
    output.append("January Wilson")
    entries.append("add Tom Draper +449182729182 tommy.d@gmail.com")
    output.append("Tom Draper")
    entries.append("list")
    output.append("1.")
    output.append("January")
    output.append("31600982184")
    output.append("jan@wilstore.com")
    output.append("2.")
    output.append("Tom")
    output.append("449182729182")
    output.append("tommy.d@gmail.com")
    entries.append("edit 1")
    output.append("1")
    output.append("January")
    output.append("31600982184")
    output.append("jan@wilstore.com")
    entries.append("")
    entries.append("+31600982185")
    entries.append("")
    output.append("updated")
    output.append("31600982185")
    entries.append("del 1")
    output.append("January")
    entries.append("list")
    output.append("2.")
    output.append("Tom")
    output.append("449182729182")
    output.append("tommy.d@gmail.com")
    entries.append("exit")

    actual_output = outputOf(stdinArgs=entries, overwriteAttributes=[("__name__", "__main__")])
    
    from_position = 0
    for expected_part in output:
        print(expected_part)
        result = actual_output.find(expected_part, from_position)
        print(result)
        assert result != -1
        from_position = result + 1
