import ast

py_file = open('../pyraya/src/raya/controllers/sound_controller.py', 'r')
node = ast.parse(py_file.read())

classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
for class_ in classes:
    print("Class name:", class_.name)
    methods = [n for n in class_.body if isinstance(n, ast.FunctionDef)]
    for method in methods:
        print("Function name:", method.name)