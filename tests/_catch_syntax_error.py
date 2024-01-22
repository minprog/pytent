import checkpy.tests as t
import re

from _static_analysis import *

@t.test(1)
def no_syntax_error(test):
    """het bestand is in orde"""
    def augment(define_location, lines):
        start = define_location
        while True:
            start -= 1
            if lines[start].strip() == "":
                start += 1
                break
            elif lines[start].startswith("  ") or lines[start].startswith("\t"):
                break
            elif start <= 0:
                break
        end = define_location
        waiting = False
        while True:
            end += 1
            if end > len(lines) - 1:
                if waiting != False:
                    end = waiting
                else:
                    end = len(lines) - 1
                break
            elif lines[end].strip() == "":
                if waiting == False:
                    waiting = end-1
                continue
            elif lines[end].startswith("  ") or lines[start].startswith("\t") or lines[start-1].endswith("\\"):
                waiting = False
                continue
            else:
                if waiting:
                    end = waiting
                else:
                    end -= 1
                break
        return start, end

    class MappedProgram():
        def __init__(self):
            with open(test.fileName, 'r') as f:
                self.lines = f.readlines()
                # print(self.lines[-1])
                self.size = len(self.lines)
            if self.size > 0:
                defs = []
                for i in range(self.size):
                    if self.lines[i].startswith('def '):
                        defs.append(i)
                augmented = [augment(define, self.lines) for define in defs]
                self.program_map = augmented
        def write_program(self):
            # print(f"writing {self.syntax_errors}")
            with open(test.fileName, 'w') as f:
                for no in range(self.size):
                    printed=False
                    for err_line in self.syntax_errors:
                        # print(f"checking for line {no} and err_line {err_line} {self.program_map}")
                        if len(list(filter(lambda i: i[0] <= no <= i[1] and i[0] <= err_line <= i[1], self.program_map))) > 0:
                            f.write(f"# {self.lines[no]}")
                            printed=True
                            break
                    if printed==False:
                        f.write(f"{self.lines[no]}")
        def remove_syntax_errors(self):
            self.syntax_errors = []
            while lineno := has_syntax_error():
                lineno -= 1
                if lineno in self.syntax_errors:
                    return
                if len(self.syntax_errors) == 4:
                    return
                self.syntax_errors.append(lineno)
                self.write_program()
                # if len(self.syntax_errors)==1:
                    # break

    def testMethod():
        p = MappedProgram()
        # print(p.program_map)
        p.remove_syntax_errors()

        if lineno := has_syntax_error():
            return False, f"er is minstens één syntax error die niet verwijderd kon worden"
        if len(p.syntax_errors) > 0:
            test.description = f"deel van code verwijderd ivm syntax errors op regel {', '.join([str(e+1) for e in p.syntax_errors])}"
        return True
    test.test = testMethod
