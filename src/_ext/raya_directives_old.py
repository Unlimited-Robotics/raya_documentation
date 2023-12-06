import os
import sys
import ast
import astunparse
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive

# PyRaYa path
PYRAYA_PATH = os.path.abspath("./pyraya/src/raya")+'/'

# Important! Documentation should be like:
# def abc(a: int, c = [1,2]):
#     """_summary_
#
#     :param int a: _description_
#     :param list c: _description_, defaults to [1,2]
#     :raises AssertionError: _description_
#     :return _type_: _description_
#     """
#     if a > 10:
#         raise AssertionError("a is more than 10")
#
#     return c


# Helper functions
def align(argument):
    """Conversion function for the "align" option."""
    return directives.choice(argument, ('left', 'center', 'right'))


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

def parse_docstring_function(doc: str):
    print(doc)
    paragraph_node = nodes.paragraph(text=doc)
    return [paragraph_node, nodes.paragraph(text="Hi")]

# Directives
class HelloWorld(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]

class RaYaDocumentation(Directive):
    required_arguments  = 2
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'alt': directives.unchanged,
                   'height': directives.nonnegative_int,
                   'width': directives.nonnegative_int,
                   'scale': directives.nonnegative_int,
                   'align': align,
                   }
    has_content = False

    def run(self):
        docstring = get_func_docstring(self.arguments[0],self.arguments[1])
        return parse_docstring_function(docstring)

def setup(app):
    app.add_directive("helloworld", HelloWorld)
    app.add_directive("rayadocumentation", RaYaDocumentation)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }