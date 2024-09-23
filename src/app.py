from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "API de agendamento de salas"

@app.route('/salas')
def todas_salas():
    return render_template('salas.html', titulo='Todas as salas')


if __name__ == '__main__':
    app.run(debug=True)