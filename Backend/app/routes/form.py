import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, "../../frontend")

filepath_home = filepath + "/pages/form.html"
filepath_static_js = filepath + "/static/form/script.js"

def static_file(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    else:
        return b"<h1>Archivo no encontrado</h1>"

def form_page():
    return static_file(filepath_home)

def static_form_js():
    return static_file(filepath_static_js)