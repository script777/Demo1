import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, "../../frontend")

filepath_home = filepath + "/pages/about.html"

def static_file(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    else:
        return b"<h1>Archivo no encontrado</h1>"

def about_page():
    return static_file(filepath_home)
