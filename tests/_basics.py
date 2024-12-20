import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _static_analysis import *

import sys
import subprocess
import re
import os

from _catch_syntax_error import *

def assert_doctest(fname, args, expected, hint=None, use_output=False):
    # check function existence
    defines_function(fname)
    f = getFunction(fname)

    # wrap args for consistent calling
    if type(args) != tuple:
        args = (args,)
    
    msg = []

    # call function
    try:
        result = f(*args)
        if use_output:
            check = f.printOutput.strip() == expected.strip()
        else:
            check = result == expected
    except:
        check = False
        msg.append("CRASH!")

    if not check:
        msg.append("voeg deze doctest toe en gebruik 'm om je code te verbeteren:")
        args = ', '.join([a.__repr__() for a in args])
        msg.append(f">>> {fname}({args})")
        if use_output:
            msg.append(expected)
        else:
            msg.append(f"{expected.__repr__()}")
        if hint:
            msg.append(f"({hint})")
        raise AssertionError('\n'.join(msg))

# @t.passed(no_syntax_error, hide=False)
# @t.test(2)
# def mypy_ok(test):
#     """type hints zijn ingevuld en consistent bevonden"""
#     def testMethod():
#         p = subprocess.run(['mypy', '--ignore-missing-imports', test.fileName], capture_output=True, universal_newlines=True)
#         return p.returncode == 0, p.stdout
#     test.test = testMethod
#     def report(output):
#         return '- line ' + '\n- line '.join([':'.join(i.split(':')[1:])[:60] for i in output.splitlines()[:-1]])
#     test.fail = report

@t.passed(no_syntax_error, hide=False)
@t.test(3)
def doctest_ok(test):
    """doctests zijn voldoende aanwezig en geven allemaal akkoord"""
    def testMethod():
        with open(test.fileName, 'r') as source_file:
            source = source_file.read()
            functions = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', source)
            n_functions_not_returning = len([function for function in functions if ('file' in function[1] or function[3] == 'None' or function[3] == '')])
        p = subprocess.run([sys.executable or 'python3', '-m', 'doctest', '-v', test.fileName], capture_output=True, universal_newlines=True)
        if "Traceback" in p.stderr:
            return False, p.stderr.splitlines()[-1]
        test_stats_rex = re.compile('(\d*) tests in (\d*) items')
        test_pass_rex = re.compile('(\d*) passed and (\d*) failed')
        test_stats = test_stats_rex.search(p.stdout.splitlines()[-3])
        test_pass = test_pass_rex.search(p.stdout.splitlines()[-2])
        n_tests = int(test_stats.group(1))
        n_items = int(test_stats.group(2))-1
        n_tested = n_items-n_functions_not_returning
        n_pass  = int(test_pass.group(1))
        if n_items == 0:
            return False, "het programma heeft geen functies"
        elif n_tested > 0 and n_tests // n_tested < 2:
            return False, f"{n_tests} voorbeelden bij {n_items} functies is niet genoeg \n    (we tellen alleen functies die iets returnen)"
        elif n_pass < n_tests:
            return False, f"{n_pass} van {n_tests} voorbeelden slagen"
        return True

    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
