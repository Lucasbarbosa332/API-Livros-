# API - E um lugara para disponibilizar recursos e/ ou funcionalidades 
# 1. objetivo - criar um API de disponibilidade de consulta, criação, exclusão de livros e edição.
# 2. URL base - localhost
# 3. Endpoint 

    #  - localhost/livros (GET)
    #  - localhost/livros (POST)
    #  - localhost/livros/ id  (GET)
    #  - localhost/livros/id  (PUT)
    #  - localhost/livros/ id (DELETE)

# 4.  Quais recusrsos - Livros 
    

from flask import Flask, jsonify, request 

app = Flask(__name__)

livros = [
    {'id': 1, 'título': 'As 48 Leis do Poder', 'autor': 'Robert Greene'},
    {'id': 2, 'título': 'Hábitos Atômicos', 'autor': 'James Clear'},
    {'id': 3, 'título': 'O Homem Mais Rico da Babilônia', 'autor': 'George S. Clason'},
    {'id': 4, 'título': 'Poder do Hábito', 'autor': 'Charles Duhigg'},
    {'id': 5, 'título': 'O Segredo', 'autor': 'Rhonda Byrne'},
    {'id': 6, 'título': 'O Milagre da Manhã', 'autor': 'Hal Elrod'},
    {'id': 7, 'título': 'O Poder da Ação', 'autor': 'Paulo Vieira'},
    {'id': 8, 'título': 'A Arte da Guerra', 'autor': 'Sun Tzu'},
    {'id': 9, 'título': 'O Poder da Mente Subconsciente', 'autor': 'Joseph Murphy'},
    {'id': 10, 'título': 'O Jeito Harvard de Ser Feliz', 'autor': 'Shawn Achor'},
    {'id': 11, 'título': 'Desperte Seu Gigante Interior', 'autor': 'Tony Robbins'},
    {'id': 12, 'título': 'A Sutil Arte de Ligar o F*da-se', 'autor': 'Mark Manson'},
    {'id': 13, 'título': 'Os Segredos da Mente Milionária', 'autor': 'T. Harv Eker'},
    {'id': 14, 'título': 'A Lei da Atração', 'autor': 'Esther e Jerry Hicks'},
    {'id': 15, 'título': 'Quem Pensa, Enriquece', 'autor': 'Napoleon Hill'},
    {'id': 16, 'título': 'Grit', 'autor': 'Angela Duckworth'},
    {'id': 17, 'título': 'A Coragem de Ser Imperfeito', 'autor': 'Brené Brown'},
    {'id': 18, 'título': 'O Obstáculo é o Caminho', 'autor': 'Ryan Holiday'},
    {'id': 19, 'título': 'Mindset: A Nova Psicologia do Sucesso', 'autor': 'Carol S. Dweck'},
    {'id': 20, 'título': 'Os 7 Hábitos das Pessoas Altamente Eficazes', 'autor': 'Stephen R. Covey'},
    {'id': 21, 'título': 'O Poder do Agora', 'autor': 'Eckhart Tolle'},
    {'id': 22, 'título': 'O Vendedor de Sonhos', 'autor': 'Augusto Cury'},
    {'id': 23, 'título': 'Quem Pensa, Enriquece', 'autor': 'Napoleon Hill'},
    {'id': 24, 'título': 'A Mente Milionária', 'autor': 'T. Harv Eker'},
    {'id': 25, 'título': 'A Magia do Pensamento Grande', 'autor': 'David Schwartz'},
    {'id': 26, 'título': 'A Lei do Triunfo', 'autor': 'Napoleon Hill'},
    {'id': 27, 'título': 'Trabalhe 4 Horas por Semana', 'autor': 'Tim Ferriss'},
    {'id': 28, 'título': 'A Chave Mestra', 'autor': 'Charles F. Haanel'},
    {'id': 29, 'título': 'O Homem que Vendeu Sua Ferrari', 'autor': 'Robin Sharma'},
    {'id': 30, 'título': 'O Poder do Subconsciente', 'autor': 'Joseph Murphy'},
    {'id': 31, 'título': 'O Monge e o Executivo', 'autor': 'James C. Hunter'},
    {'id': 32, 'título': 'A Verdade sobre o Sucesso', 'autor': 'Jack Canfield'},
    {'id': 33, 'título': 'O Jeito Google de Trabalhar', 'autor': 'Eric Schmidt, Jonathan Rosenberg'},
    {'id': 34, 'título': 'A Arte de Fazer Acontecer', 'autor': 'David Allen'},
    {'id': 35, 'título': 'Como Fazer Amigos e Influenciar Pessoas', 'autor': 'Dale Carnegie'},
    {'id': 36, 'título': 'Vença a Si Mesmo', 'autor': 'Brendon Burchard'},
    {'id': 37, 'título': 'O Milionário Mora ao Lado', 'autor': 'Thomas Stanley e William Danko'},
    {'id': 38, 'título': 'Essencialismo: A disciplinada busca por menos', 'autor': 'Greg McKeown'},
    {'id': 39, 'título': 'A Arte de Lidar com Pessoas', 'autor': 'Dale Carnegie'},
    {'id': 40, 'título': 'A Mente Organizada', 'autor': 'Daniel Levitin'},
    {'id': 41, 'título': 'O Andar do Bêbado', 'autor': 'Leonard Mlodinow'},
    {'id': 42, 'título': 'A Mente do Futuro', 'autor': 'Erik Brynjolfsson'},
    {'id': 43, 'título': 'O Segredo da Mente Milionária', 'autor': 'T. Harv Eker'},
    {'id': 44, 'título': 'Como Ter Uma Vida Extraordinária', 'autor': 'Gustavo Cerbasi'},
    {'id': 45, 'título': 'Vença a Procrastinação', 'autor': 'Piers Steel'},
    {'id': 46, 'título': 'O Poder do Não', 'autor': 'James Altucher'},
    {'id': 47, 'título': 'O Dinheiro ou a Vida', 'autor': 'Joe Dominguez, Vicki Robin'},
    {'id': 48, 'título': 'A Estratégia do Oceano Azul', 'autor': 'W. Chan Kim, Renée Mauborgne'},
    {'id': 49, 'título': 'Comece Pelo Porquê', 'autor': 'Simon Sinek'},
    {'id': 50, 'título': 'Criatividade S.A.', 'autor': 'Ed Catmull'},
    {'id': 51, 'título': 'Foco', 'autor': 'Daniel Goleman'},
    {'id': 52, 'título': 'A Lei da Atração', 'autor': 'Esther Hicks'},
    {'id': 53, 'título': 'Liderança: A 5ª Disciplina', 'autor': 'Peter Senge'},
    {'id': 54, 'título': 'Liderança em Alta Performance', 'autor': 'Jim Collins'},
    {'id': 55, 'título': 'Nunca Almoce Sozinho', 'autor': 'Keith Ferrazzi'},
    {'id': 56, 'título': 'A Arte de Liderar', 'autor': 'Maxwell John'},
    {'id': 57, 'título': 'Pessoas também são Negócios', 'autor': 'David Ulrich'},
    {'id': 58, 'título': 'Psicologia das Cores', 'autor': 'Eva Heller'},
    {'id': 59, 'título': 'O Jeito Pixar de Contar Histórias', 'autor': 'David Price'},
    {'id': 60, 'título': 'Liderança é uma Jornada', 'autor': 'Ken Blanchard'},
    
    
    {'id': 61, 'título': 'O Poder do Foco', 'autor': 'Jack Canfield, Mark Victor Hansen e Les Hewitt'},
    {'id': 62, 'título': 'A Mente Milionária', 'autor': 'T. Harv Eker'},
    {'id': 63, 'título': 'A Arte da Felicidade', 'autor': 'Dalai Lama'},
    {'id': 64, 'título': 'Geração de Riqueza', 'autor': 'Carlos Wizard Martins'},
    {'id': 65, 'título': 'Desafios da Vida', 'autor': 'Augusto Cury'},
    {'id': 66, 'título': 'A Ciência de Ficar Rico', 'autor': 'Wallace D. Wattles'},
    {'id': 67, 'título': 'O Segredo das Mentes Brilhantes', 'autor': 'John C. Maxwell'},
    {'id': 68, 'título': 'Desperte o Gigante Interior', 'autor': 'Tony Robbins'},
    {'id': 69, 'título': 'Como Mudar Sua Mente', 'autor': 'Michael Pollan'},
    {'id': 70, 'título': 'O Poder da Empatia', 'autor': 'Karla McLaren'},
    {'id': 71, 'título': 'O Segredo da Mente Milionária', 'autor': 'T. Harv Eker'},
    {'id': 72, 'título': 'Seja Foda!', 'autor': 'Caio Carneiro'},
    {'id': 73, 'título': 'O Código da Mente Extraordinária', 'autor': 'Dr. Vishen Lakhiani'},
    {'id': 74, 'título': 'Gestão da Emoção', 'autor': 'Daniel Goleman'},
    {'id': 75, 'título': 'Dobre Seus Lucros', 'autor': 'Bob Fifer'},
    {'id': 76, 'título': 'O Método Bullet Journal', 'autor': 'Ryder Carroll'},
    {'id': 77, 'título': 'A Vida é Curta', 'autor': 'Javier Cercas'},
    {'id': 78, 'título': 'Você Pode Curar Sua Vida', 'autor': 'Louise Hay'},
    {'id': 79, 'título': 'O Lado Difícil das Situações Difíceis', 'autor': 'Ben Horowitz'},
    {'id': 80, 'título': 'O Poder da Ação', 'autor': 'Paulo Vieira'},
    {'id': 81, 'título': 'Meditações', 'autor': 'Marco Aurélio'},
    {'id': 82, 'título': 'A Fórmula da Riqueza', 'autor': 'Wallace D. Wattles'},
    {'id': 83, 'título': 'Comece pelo Porquê', 'autor': 'Simon Sinek'},
    {'id': 84, 'título': 'Desperte para a Vida', 'autor': 'Eckhart Tolle'},
    {'id': 85, 'título': 'O Impacto da Felicidade', 'autor': 'Shawn Achor'},
    {'id': 86, 'título': 'O Grande Livro do Marketing Pessoal', 'autor': 'Felipe Lima'},
    {'id': 87, 'título': 'Atitude Mental Positiva', 'autor': 'Napoleon Hill'},
    {'id': 88, 'título': 'O Poder do Não', 'autor': 'James Altucher'},
    {'id': 89, 'título': 'A Filosofia do Sucesso', 'autor': 'Jack Canfield'},
    {'id': 90, 'título': 'O Caminho do Guerreiro Pacífico', 'autor': 'Dan Millman'},
    {'id': 91, 'título': 'A Vida no Controle', 'autor': 'Tony Robbins'},
    {'id': 92, 'título': 'Atitude Empreendedora', 'autor': 'José Dornelas'},
    {'id': 93, 'título': 'A Mente que Vence', 'autor': 'Carol S. Dweck'},
    {'id': 94, 'título': 'A Fórmula da Felicidade', 'autor': 'Dan Gilbert'},
    {'id': 95, 'título': 'O Sucesso é para Todos', 'autor': 'Roberto Shinyashiki'},
    {'id': 96, 'título': 'Riqueza e Prosperidade', 'autor': 'Phil Town'},
    {'id': 97, 'título': 'A Arte de Pensar Claramente', 'autor': 'Rolf Dobelli'},
    {'id': 98, 'título': 'Superando o Medo', 'autor': 'Susan Jeffers'},
    {'id': 99, 'título': 'A Mente Vencedora', 'autor': 'J. Martin'},
    {'id': 100, 'título': 'Desafio das 5 Oportunidades', 'autor': 'João Kepler'}
]

# Consultar todos os livros
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar livro por ID
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Editar livro por ID
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    return jsonify({'erro': 'Livro não encontrado'}), 404

# Incluir novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    if 'título' not in novo_livro or 'autor' not in novo_livro:
        return jsonify({'erro': 'Dados inválidos, título e autor são obrigatórios'}), 400
    novo_livro['id'] = len(livros) + 1  # Garante um ID único e incremental
    livros.append(novo_livro)
    return jsonify(novo_livro), 201  # Retorna o livro criado com status 201

# Excluir livro
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({'mensagem': 'Livro excluído com sucesso'}), 204  # Retorna 204 No Content
    return jsonify({'erro': 'Livro não encontrado'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
