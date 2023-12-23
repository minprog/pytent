import checkpy.tests as t


@t.test()
def remove_main(test):
    """removing any main or testing code"""
    def testMethod():
        # read original file
        with open(test.fileName, 'r') as f:
            file_contents = f.readlines()
        
        # rewrite file, removing any code between defs as well as the main
        with open(test.fileName, 'w') as f:
            state = 0
            for line in file_contents:
                if state == 0:
                    if line.startswith('def '):
                        state = 1
                    f.write(line)
                elif state == 1:
                    if not (line.strip() == '' or line.startswith(' ') or line.startswith("\t") or line.startswith("def ") or line.startswith("#") or line.find("->") >= 0):
                        state = 2
                        continue
                    f.write(line)
                elif state == 2:
                    if line.startswith('def '):
                        f.write(line)
                        state = 1
                    else:
                        f.write(f"# {line}")
    test.test = testMethod
