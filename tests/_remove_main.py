import checkpy.tests as t


@t.test()
def remove_main(test):
    """verwijderen van main of andere testcode"""
    def testMethod():
        # read original file
        with open(test.fileName, 'r') as f:
            file_contents = f.readlines()
        
        # rewrite file, removing any code between defs as well as the main
        with open(test.fileName, 'w') as f:
            state = 0
            for line in file_contents:
                if state == 0:
                    # before first function: take everything, including first 'def' line
                    if line.startswith('def '):
                        state = 1
                    f.write(line)
                elif state == 1:
                    # function: take everything
                    if line.startswith('"""'):
                        f.write(line)
                        state = 3
                        continue
                    if not (line.strip() == '' or line.startswith(' ') or line.startswith("\t") or line.startswith("def ") or line.startswith("#") or line.find("->") >= 0):
                        f.write(f"# {line}")
                        state = 2
                        continue
                    f.write(line)
                elif state == 2:
                    # after function: skip everything
                    if line.startswith('#'):
                        f.write(line)
                    elif line.startswith('"""'):
                        f.write(line)
                        state = 3
                    elif not line.startswith('def '):
                        f.write(f"# {line}")
                    else:
                        f.write(line)
                        state = 1
                elif state == 3:
                    f.write(line)
                    if line.endswith('"""'):
                        state = 2

    test.test = testMethod
