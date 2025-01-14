from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados (para SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.db'  # Banco de dados local em SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar o rastreamento de modificações (não é necessário)

# Inicializar o banco de dados
db = SQLAlchemy(app)

# Definição do modelo (tabela) de livros
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    título = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Livro {self.título} - {self.autor}>"

# Criar o banco de dados e as tabelas (use somente uma vez no início)
with app.app_context():
    db.create_all()

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = Livro.query.all()  # Obtém todos os livros do banco de dados
    return jsonify([{'id': livro.id, 'título': livro.título, 'autor': livro.autor} for livro in livros])

# Consultar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = Livro.query.get(id)  # Obtém o livro pelo ID
    if livro:
        return jsonify({'id': livro.id, 'título': livro.título, 'autor': livro.autor})
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    livro = Livro.query.get(id)
    if livro:
        livro.título = livro_alterado.get('título', livro.título)
        livro.autor = livro_alterado.get('autor', livro.autor)
        db.session.commit()  # Salva as alterações no banco
        return jsonify({'id': livro.id, 'título': livro.título, 'autor': livro.autor})
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    if 'título' not in novo_livro or 'autor' not in novo_livro:
        return jsonify({'erro': 'Dados inválidos, título e autor são obrigatórios'}), 400
    livro = Livro(título=novo_livro['título'], autor=novo_livro['autor'])
    db.session.add(livro)  # Adiciona o novo livro ao banco de dados
    db.session.commit()  # Salva no banco de dados
    return jsonify({'id': livro.id, 'título': livro.título, 'autor': livro.autor}), 201

# Excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    livro = Livro.query.get(id)
    if livro:
        db.session.delete(livro)  # Exclui o livro do banco de dados
        db.session.commit()  # Salva a alteração
        return jsonify({'mensagem': 'Livro excluído com sucesso'}), 204
    return jsonify({'erro': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
