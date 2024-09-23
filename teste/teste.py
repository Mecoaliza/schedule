from flask import Flask, render_template
from ssl import SSLContext, PROTOCOL_TLS_SERVER
#pip install flash==2.0.2
"""
Código para gerar um certificado digital, deve ser executado na mesma pasta do projeto.

openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt

Obs: Programa Wireshark para testar a segurança
"""

app = Flask(__name__)


# Cria um contexto SSL
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='server.crt', keyfile='server.key')

@app.route('/inicio')
def ola():
    return render_template('listas.html', titulo='Jogos')


# Inicia o servidor com HTTPS
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
    #app.run(host='0.0.0.0', port=8080)  #permitir acessos externos à aplicação host='0.0.0.0'
#app.run()