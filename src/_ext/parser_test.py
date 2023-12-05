import os
import sys
import ast
import astunparse

PYRAYA_PATH = os.path.abspath("./pyraya/src/raya")+'/'

def get_func_docstring(file:str, fun_name:str):
    py_file = open(PYRAYA_PATH+file, 'r')
    node = ast.parse(py_file.read())
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    if not len(classes) > 1:
        classes.append(node.body)
    for class_ in classes:
        methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
        for method in methods:
            if method.name == fun_name:
                return ast.get_docstring(method)


docstring = get_func_docstring("/controllers/leds_controller.py", "get_colors")
docstring_parts = docstring.split('\n\n')
print(docstring_parts)