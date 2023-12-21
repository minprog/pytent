from checkpy import *
from _basics import *

@t.test()
def data_proc():
    """data_cleanup werkt correct"""
    def testMethod():
        with open('data.csv', 'w') as data_csv:
            data_csv.write('1,10.0,5.5')
            data_csv.write('2,-,3.0')
            data_csv.write('3,1.0,-')

        output = lib.outputOf(test.fileName, stdinArgs=[7, 9.5],
                    overwriteAttributes = [("__name__", "__main__")])

        with open('clean_data.csv', 'r') as clean_data_csv:
            clean_data = clean_data_csv.read()
        
        return asserts.exact(clean_data.strip(),
        "1,10.0,5.5\n2,7.0,3.0\n3,1.0,9.5\nGemiddelde zonder verbeteringen,5.5,4.25\nGemiddelde met verbeteringen,6.0,6.0")
    test.test = testMethod
