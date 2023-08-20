import http.server
import random
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Gere um número aleatório entre 0 e 99.
        random_number = random.randint(0, 99)

        # Se o número for menor ou igual a 94 (95% das vezes), retorne "Autorizado".
        if random_number <= 94:
            response_data = {"message": "Autorizado"}
        # Caso contrário, retorne "Negado".
        else:
            response_data = {"message": "Negado"}

        # Configurar cabeçalhos de resposta.
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        # Enviar o JSON como resposta.
        self.wfile.write(json.dumps(response_data).encode())

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print('Servidor rodando na porta 8080...')
    httpd.serve_forever()
