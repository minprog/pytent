from checkpy import *
from typing import Any
import ast

from checkpy import static

def extract_function_by_name(function_name):
    # Parse the source code into an AST
    source_code = static.getSource()
    tree = ast.parse(source_code)

    # Find the function definition with the given name
    target_function = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            target_function = node
            break

    if target_function is None:
        return f"Function '{function_name}' not found."

    # Extract the source code lines based on line numbers
    start_lineno = target_function.lineno - 1
    end_lineno = target_function.end_lineno
    function_source = "\n".join(source_code.splitlines()[start_lineno:end_lineno])

    return function_source

def no_string_methods_or_slicing(src) -> bool:
    """
    Vind aanroepen naar ingebouwde string methodes en slicing.
    Returned een error bericht met de gebruikt methode of slicing en op welke regel.
    Returned None als er er niks aan de hand is :)
    """
    # src = static.getSource()
    method_names = [n for n in dir("") if not n.startswith("__")]

    lines = src.split("\n")
    for method_name in method_names:
        for line_nr, line in enumerate(lines):
            if "." + method_name in line:
                raise AssertionError(f"Gebruik van string-methodes is niet toegestaan. Zoals {method_name} op regel {line_nr + 1}:\n{line}")

    import ast
    class Visitor(ast.NodeVisitor):
        def visit_Slice(self, node: ast.Slice):
            raise AssertionError(f"Gebruik van slicing is niet toegestaan. Zoals op regel {node.lineno}:\n{lines[node.lineno - 1]}")

    tree = ast.parse(src)
    visitor = Visitor()
    visitor.visit(tree)
    return True

def has_no_call_to(src, *banned_calls) -> bool:
    found = False

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            if node.id in banned_calls:
                nonlocal found
                found = True

    calls: list[ast.Call] = static.getAstNodes(ast.Call, source=src)
    for call in calls:
        Visitor().visit(call)

    if found:
        raise AssertionError(f"Gebruik van de functie {banned_calls[0]}() is niet toegestaan")

    return not found

def defines_function(name: str) -> bool:
    check = name in static.getFunctionDefinitions()
    if not check:
        raise AssertionError(f"`{name}` is niet aanwezig")
    return check

def defines_function_no_assert(name: str) -> bool:
    check = name in static.getFunctionDefinitions()
    return check

def not_in_code(construct: type):
    check = construct not in static.AbstractSyntaxTree()
    name = str(construct).split(".")[1].split("'")[0].lower()
    if not check:
        if name in ['list', 'set', 'tuple', 'dict']:
            raise AssertionError(f"{name}s mogen niet gebruikt worden in deze opdracht")
        else:
            raise AssertionError(f"`{name}` mag niet gebruikt worden in deze opdracht")
    return check

def in_code(construct: type):
    check = construct in static.AbstractSyntaxTree()
    name = str(construct).split(".")[1].split("'")[0].lower()
    if not check:
        raise AssertionError(f"`{name}` moet gebruikt worden in deze opdracht")
    return check

def has_syntax_error():
    try:
        compile(static.getSource(), "<your program>", "exec")
    except SyntaxError as error:
        return error.lineno
    return False

def has_string(*forbidden_strings):
    source = static.getSource()
    return any(f in source for f in forbidden_strings)

def has_call(*banned_calls) -> bool:
    found = False

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            if node.id in banned_calls:
                nonlocal found
                found = True

    calls: list[ast.Call] = static.getAstNodes(ast.Call)
    for call in calls:
        Visitor().visit(call)

    return found

def has_import(*banned_imports) -> bool:
    imports: list[ast.Import] = static.getAstNodes(ast.Import)
    for imp in imports:
        names = [alias.name for alias in imp.names]
        for name in names:
            if name in banned_imports:
                return True

    imports_from: list[ast.ImportFrom] = static.getAstNodes(ast.ImportFrom)
    for imp in imports_from:
        for name in imp.names:
            if name in banned_imports:
                return True

    return False

def has_generators() -> bool:
    return static.getAstNodes(ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)

#----

def not_defines_function(name: str) -> bool:
    check = name not in static.getFunctionDefinitions()
    if not check:
        raise AssertionError(f"`{name}` is onverwacht aanwezig")
    return check

def not_has_stringmethods() -> bool:
    tree = ast.parse(static.getSource())
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if n.func.attr in ['replace', 'find']:
                raise AssertionError(f"string-methods zoals {n.func.attr}() mogen niet gebruikt worden")
    return True

def not_has_stringmult() -> bool:
    tree = ast.parse(static.getSource())
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            if (isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
                or isinstance(n.right, ast.Constant) and isinstance(n.right.value, str)):
                raise AssertionError(f"`*` mag alleen gebruikt worden om getallen te vermenigvuldigen met elkaar")
    return True
