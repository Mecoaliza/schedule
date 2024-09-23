from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "API de agendamento de salas"

@app.post('/salas')
def cadastrar_salas():
    dados= request.json
    nome_sala = dados.get('nome')
    capacidade = dados.get('capacidade')

    if not nome_sala or not capacidade:
        return jsonify({"erro": "Nome da sala e capacidade são obrigatórios!"}), 400
    
    # Simulação de inserção em banco
    return jsonify({
        "mensagem": "Sala cadastrada com sucesso!",
        "sala": {
            "nome": nome_sala,
            "capacidade": capacidade
        }
    }), 201



if __name__ == '__main__':
    app.run(debug=True)