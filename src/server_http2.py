from hyper import HTTP20Connection
from hyper.http20.response import Response
from flask import Flask, send_from_directory

def serve_static(path):
    return send_from_directory('build', path)

def handle_request(conn, stream_id, headers, body):
    # Processa a requisição
    # ...

    # Cria a resposta
    response_headers = [
        (':status', '200'),
        ('content-type', 'text/plain'),
    ]
    response_body = b'Hello, HTTP/2!'

    # Envia a resposta
    conn.send_response(stream_id, response_headers, response_body)

def main():
    conn = HTTP20Connection('localhost', 3002)
    conn.connect()

    # Define o handler para requisições
    conn.data_received_callback = handle_request

    # Loop para receber e processar requisições
    while True:
        conn.receive_data()

if __name__ == '__main__':
    main()