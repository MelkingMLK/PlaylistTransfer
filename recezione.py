from flask import Flask, request

app = Flask(__name__)

@app.route('/recezione.py', methods=['GET'])
def ricevi_dati():
    # Ricevi parametri GET
    nome = request.args.get('nome')
    eta = request.args.get('età')
    return f"Ricevuto: Nome = {nome}, Età = {eta}"

if __name__ == '__main__':
    app.run(debug=True)