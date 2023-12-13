import os
import re
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

class RayaDocstringFunctionFormatter():

    def __init__(self, docstring: str) -> None:
        # print(docstring)
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
                self.params_list = [(p[0],p[1],p[2].split(", defaults to")[0]\
                                    .replace(' ','') \
                                    if len(p[2].split(", defaults to"))>1 \
                                    else p[2], 
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
                self.raises_list = []
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

rayadoc = RayaDocstringFunctionFormatter(get_func_docstring("/controllers/leds_controller.py", "get_colors"))
print(rayadoc.description)
print(rayadoc.params_list)
print(rayadoc.raises_list)
print(rayadoc.func_return)


# txt = get_func_docstring("/controllers/leds_controller.py", "get_colors")
# description = txt.split('\n\n')[0]
# x = re.split(":param\s+", txt.split('\n\n')[1], flags=re.M)
# print([clear.split('\n:')[0].replace('\n','') for clear in x])
# for text in txt.split('\n\n')[1].split('\n'):
#     x = re.split(":param\s+\w+\s+\w+:+[A-Za-z]+(\r\n|\r|\n)", text, flags=re.M)
#     print(x)