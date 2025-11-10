from Backend.app.routes.controller import Handler
from http.server import ThreadingHTTPServer

PORT = 8000

def run(handler_class=Handler):
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, handler_class)
    print(f"Servidor corriendo en http://localhost:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nApagando servidor...")
    finally:
        httpd.server_close()
        print("Servidor detenido correctamente.")

if __name__ == "__main__":
    run()
    