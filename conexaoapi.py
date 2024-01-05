from flask import Flask

app = Flask(__name__)

@app.route('/api/consumir-tabela', methods=['GET'])
def consumir_tabela():
    # Lógica para consumir a tabela do Databricks aqui
    
    # Retorna "OK"
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
