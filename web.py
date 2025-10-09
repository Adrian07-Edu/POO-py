# servidor_con_extension_html_omitida.py
from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Si la URL no tiene extensión y no termina en "/"
        if not os.path.splitext(self.path)[1] and not self.path.endswith('/'):
            # Intenta agregar ".html" al final
            possible_path = self.path + ".html"
            if os.path.exists(self.translate_path(possible_path)):
                self.path = possible_path

        # Llama al manejador base para procesar la solicitud
        return super().do_GET()

def run(server_class: type[HTTPServer] = HTTPServer, handler_class: type[BaseHTTPRequestHandler] = CustomHandler, port: int = 80, directory: str = "web"):
    os.chdir(directory)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor iniciado en http://localhost:{port} (sirviendo desde /{directory}/)")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
