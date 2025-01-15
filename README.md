# 📚 API de Livros com Flask

Bem-vindo(a) à **API de Livros**! 🚀  
Esta aplicação permite gerenciar uma coleção de livros usando Flask e SQLite.  
Confira abaixo como configurar, usar e contribuir com o projeto. 🎉

---

## 🛠️ Configuração do Projeto

### Pré-requisitos
Antes de começar, certifique-se de ter instalado:
- **Python 3.8+**
- **pip** (gerenciador de pacotes do Python)

### Instalando Dependências

  1. Clone este repositório:
   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

  2. Navegue até a pasta do projeto:
   ```
      cd api-livros
   ```
  3. Instale as dependências:
   ```
      pip install -r requirements.txt
   ```
## Configurando o Banco de Dados

  Antes de executar a aplicação, inicialize o banco de dados:

   ```
python
>>> from app import db
>>> db.create_all()
>>> exit()
  ```
# 🚀 Endpoints Disponíveis


## 📖 Consultar Todos os Livros

<img width=40% src="https://github.com/Lucasbarbosa332/API-Livros-/blob/main/img/Metedo%20GET.png?raw=true" alt="0">

 * GET /livros
 * Descrição: Retorna uma lista com todos os livros cadastrados.
 * Exemplo de Resposta:
 ```
[
  {"id": 1, "título": "Dom Quixote", "autor": "Miguel de Cervantes"},
  {"id": 2, "título": "1984", "autor": "George Orwell"}
]
```
## 🔍 Consultar Livro por ID

  * GET /livros/<int:id>
  * Descrição: Retorna os detalhes de um livro específico.
  * Exemplo de Resposta:
```
{"id": 1, "título": "Dom Quixote", "autor": "Miguel de Cervantes"}

```


## ✍️ Editar Livro

<img width=40% src="" alt="0">

 * PUT /livros/<int:id>
 * Descrição: Atualiza os dados de um livro.
 * Corpo da Requisição:
```
{"título": "Novo Título", "autor": "Novo Autor"}

```
 * Exemplo de resposta:

```
{"id": 1, "título": "Novo Título", "autor": "Novo Autor"}

```
## ➕ Adicionar Livro

<img width=40% src="" alt="0">

 * POST /livros
 * Descrição: Adiciona um novo livro ao banco de dados.
 * Corpo da Requisição
   ```
   {"título": "Dom Quixote", "autor": "Miguel de Cervantes"}

   ```
  * Exemplo de resposta:

  ```
   {"id": 1, "título": "Dom Quixote", "autor": "Miguel de Cervantes"}


   ```
##  ❌ Excluir Livro

<img width=40% src="" alt="0">

 * DELETE /livros/<int:id>
 * Descrição: Remove um livro do banco de dados.
 * Exemplo de Resposta:

 ```
  {"mensagem": "Livro excluído com sucesso"}

 ```



