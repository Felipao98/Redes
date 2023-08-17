import http.server
import socketserver

PORT = 8000 #porta = 8000 por padrao
DIRECTORY = "home/acog24/acog24/Área de Trabalho/Redes/TP_redes"

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor rodando na porta", PORT)
    httpd.serve_forever()
