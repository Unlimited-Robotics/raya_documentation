import os
import re
import ast
import astunparse
from sphinx.parsers import RSTParser
from docutils.frontend import OptionParser
from sphinx.util.docutils import SphinxDirective
from docutils.utils import new_document


# Important! Documentation should be like:
# def abc(a: int, c = [1,2]):
#     """
#     _summary_
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

class RayaDocstringFunctionFormatter():

    def __init__(self, docstring: str) -> None:
        try:
            self.description = docstring.split('\n\n')[0]
            docstring_parts = docstring[docstring.find('\n\n')+2:].\
                replace('\n\n', '\n')
            # Params
            try:
                params = [(p.split(' ')[0], \
                                p.split(' ')[1][:-1], \
                                p.split(': ')[1]) 
                                    for p in \
                                        [p.split('\n:')[0].replace('\n','') \
                                        for p in \
                                            re.split(":param\s+", \
                                                    docstring_parts)[1:]]]
                self.params_list = [(p[0],p[1],p[2], 
                                p[2].split(", defaults to")[1].replace(' ','')
                                if len(p[2].split(", defaults to"))>1 else '') 
                                for p in params]
            except IndexError:
                self.params_list = []
            except:
                raise Exception("Wrong parameter format definition")
            
            # Exceptions
            try:
                self.raises_list = [(p.split(': ')[0], \
                            p.split(': ')[1])
                                for p in \
                                    [p.split('\n:')[0].replace('\n','') \
                                    for p in \
                                        re.split(":raises\s+", \
                                                docstring_parts)[1:]]]
            except IndexError:
                self.return_list = []
            except:
                raise Exception("Wrong exception format definition")
            
            # Return
            try:
                self.func_return = [(p.split(': ')[0], \
                            p.split(': ')[1])
                                for p in \
                                    [p.split('\n:')[0].replace('\n','') \
                                    for p in \
                                        re.split(":return\s+", \
                                                docstring_parts)[1:]]]
            except IndexError:
                self.func_return = None
            except:
                raise Exception("Wrong return format definition")
        except:
            raise Exception("Docstring bad format!")

class RayaDirective(SphinxDirective):

    PYRAYA_PATH = os.path.abspath("./pyraya/src/raya")+'/'

    def parse_rst(self, text):
        parser = RSTParser()
        parser.set_application(self.env.app)

        settings = OptionParser(
            defaults=self.env.settings,
            components=(RSTParser,),
            read_config_files=True,
        ).get_default_values()
        document = new_document("<rst-doc>", settings=settings)
        parser.parse(text, document)
        return document.children
    
    
    def get_func_docstring(self, file:str, fun_name:str):
        py_file = open(self.PYRAYA_PATH+file, 'r')
        node = ast.parse(py_file.read())
        classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
        if not len(classes) > 1:
            classes.append(node.body)
        for class_ in classes:
            m_list = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
            for method in m_list:
                if method.name == fun_name:
                    return ast.get_docstring(method)

class RayaDocumentationFunction(RayaDirective):
    required_arguments  = 2
    has_content = True

    def run(self) -> list:
        rst = ""
        docstring = self.get_func_docstring(self.arguments[0],self.arguments[1])
        rayadoc = RayaDocstringFunctionFormatter(docstring)
        print(rst)
        print(docstring)
        return self.parse_rst(rst)

def setup(app: object) -> dict:
    app.add_directive("rayadocumentationfunction", RayaDocumentationFunction)