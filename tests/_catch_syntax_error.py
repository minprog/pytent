import checkpy.tests as t
import re

from _static_analysis import *

@t.test(1)
def no_syntax_error(test):
    """het bestand is in orde"""

    class MappedProgram():
        def __init__(self):
            with open(test.fileName, 'r') as f:
                self.lines = f.readlines()
                self.size = len(self.lines)
            if self.size > 0:
                self.generate_map()
        def generate_map(self):
            self.program_map = []
            state = 0
            function_start_line = 0
            for line_no, line in enumerate(self.lines):
                # print(line_no, state)
                if state == 0:
                    # before first function: take everything, including first 'def' line
                    if line.startswith('def '):
                        function_name = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', line)[0][0]
                        function_start_line = line_no+1
                        state = 1
                elif state == 1:
                    # function: take everything
                    if line.startswith('"""'):
                        state = 3
                    elif line.startswith("def "): #not (line.strip() == '' or line.startswith(' ') or line.startswith("\t") or line.startswith("def ") or line.startswith("#") or line.find("->") >= 0):
                        # function ends now
                        # print("END")
                        function_end_line = line_no
                        self.program_map.append((function_start_line, function_end_line))
                        function_name = re.findall(r'def\s+(\w+)\(([^\)]*)\)[^-]+(->\s*([\w\[,\] _]+))?:', line)[0][0]
                        function_start_line = line_no+1
                        state = 1
                elif state == 2:
                    # after function: skip everything
                    if line.startswith('#'):
                        pass
                    elif line.startswith('"""'):
                        state = 3
                    elif not line.startswith('def '):
                        pass
                    else:
                        state = 1
                elif state == 3:
                    # inside rogue docstring
                    if line.endswith('"""'):
                        state = 2
            function_end_line = line_no
            if function_start_line != 0:
                self.program_map.append((function_start_line, function_end_line))
        def write_program(self):
            with open(test.fileName, 'w') as f:
                for no in range(1, self.size):
                    for err_line in self.syntax_errors:
                        if len(list(filter(lambda i: no >= i[0] and no <= i[1] and err_line >= i[0] and err_line <= i[1], self.program_map))) > 0:
                            f.write(f"# {self.lines[no-1]}")
                            break
                        f.write(f"{self.lines[no-1]}")
        def remove_syntax_errors(self):
            self.syntax_errors = []
            while lineno := has_syntax_error():
                if lineno in self.syntax_errors:
                    return
                if len(self.syntax_errors) == 4:
                    return
                self.syntax_errors.append(lineno)
                self.write_program()
                # return

    def testMethod():
        p = MappedProgram()
        # print(p.program_map)
        p.remove_syntax_errors()

        if lineno := has_syntax_error():
            return False, f"er is minstens één syntax error die niet verwijderd kon worden"
        if len(p.syntax_errors) > 0:
            test.description = f"functies verwijderd met syntax errors op regel {','.join([str(e) for e in p.syntax_errors])}"
        return True
    test.test = testMethod
