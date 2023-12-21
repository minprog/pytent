import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _static_analysis import *

import sys
import subprocess
import re
import os

@t.test(1)
def no_syntax_error(test):
    """het bestand is in orde"""
    def testMethod():
        if lineno := has_syntax_error():
            return False, f"de code bevat een syntax error op regel {lineno}"
        return True
    test.test = testMethod

@t.passed(no_syntax_error, hide=False)
@t.test(2)
def no_forbidden(test):
    """het bestand bevat geen sorted, map, eval, zip of comprehensions"""
    def testMethod():
        if has_call('sorted'):
            return False, "let op dat je geen sorted() gebruikt"
        if has_call('map'):
            return False, "let op dat je geen map() gebruikt"
        if has_call('eval'):
            return False, "let op dat je geen eval() gebruikt"
        if has_call('zip'):
            return False, "let op dat je geen zip() gebruikt"
        if has_generators():
            return False, "let op dat je geen [... for ...] gebruikt"
        return True
    test.test = testMethod

@t.passed(no_syntax_error, hide=False)
@t.test(3)
def mypy_ok(test):
    """type hints zijn ingevuld en consistent bevonden"""
    def testMethod():
        p = subprocess.run(['mypy', '--ignore-missing-imports', test.fileName], capture_output=True, universal_newlines=True)
        return p.returncode == 0, p.stdout
    test.test = testMethod
    def report(output):
        return '- line ' + '\n- line '.join([':'.join(i.split(':')[1:])[:60] for i in output.splitlines()[:-1]])
    test.fail = report

@t.passed(no_syntax_error, hide=False)
@t.test(4)
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
