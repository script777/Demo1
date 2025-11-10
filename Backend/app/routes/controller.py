from http.server import BaseHTTPRequestHandler

from routes.home import home_page, static_home_js
from routes.about import about_page
from routes.form import form_page, static_form_js

import json

routes_get = {
    ("GET", "/"): home_page,
    ("GET", "/static/home/script.js"): static_home_js,
    
    ("GET", "/about"): about_page,
    #("GET", "/static/home/script.js"): static_home_js,
    
    ("GET", "/form"): form_page,
    ("GET", "/static/form/script.js"): static_form_js,
}

routes_post = {
    ("POST", "/form"): form_page,
    ("POST", "/static/form/script.js"): static_form_js,
}

class Handler (BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    
    def do_GET(self):
        handler = routes_get.get(("GET", self.path))
        
        if handler:
            content = handler()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_response(404)
            self.end_headers()
            print(self.path) 
            self.wfile.write(b"<h1>Ha ocurrido un error la pagina no fue encontrada<h1>")
           
            
    def do_POST(self):
        handler = routes_post.get(("POST", self.path))
        self.path = handler
        
        if handler:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            message = {"message": "recibido cambio"}
            response = {"message": "mensaje recibido correctamente"}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            print(self.path) 
            self.wfile.write(b"<h1>Ha ocurrido un error la pagina no fue encontrada<h1>")
           

