from checkpy import *
from _catch_syntax_error import *

import os

@t.passed(no_syntax_error, hide=False)
@t.test()
def data_proc():
    """data_proc werkt correct"""
    assert has_call('open'), "bevat geen code om een bestand te openen"

    with open('data2.csv', 'w') as data_csv:
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')
        data_csv.write('\n')

    if os.access('clean_data.csv', os.F_OK):
        os.remove('clean_data.csv')

    graph = outputOf(stdinArgs=[1], overwriteAttributes=[("__name__", "__main__")])
    assert graph.strip() == '1.00-3.25 | ##\n 3.25-5.50 | ###\n 5.50-7.75 | #\n7.75-10.00 | ####'

    if os.access('clean_data.csv', os.F_OK):
        os.remove('clean_data.csv')

    graph = outputOf(stdinArgs=[2], overwriteAttributes=[("__name__", "__main__")])
    assert graph.strip() == '1.00-3.25 | ####\n 3.25-5.50 | ####\n 5.50-7.75 | #\n7.75-10.00 |'

    if os.access('clean_data.csv', os.F_OK):
        os.remove('clean_data.csv')
