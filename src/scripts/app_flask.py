import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g
import os

# Configuração
DATABASE = 'src/data/biblioteca.db'
# Define o caminho absoluto para a pasta 'templates'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..'))
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, 'templates')

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_segura' # Necessário para o Flask

# Função para obter a conexão com o banco de dados
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Configura o sqlite3 para retornar linhas como dicionários (útil para Jinja2)
        db.row_factory = sqlite3.Row
    return db

# Função para fechar a conexão com o banco de dados
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Rota principal: Listar livros (GET) e Adicionar novo livro (POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    db = get_db()
    
    if request.method == 'POST':
        # Lógica para adicionar um novo livro
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano_publicacao = request.form['ano_publicacao']
        
        try:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO livros (titulo, autor, ano_publicacao) VALUES (?, ?, ?)",
                (titulo, autor, ano_publicacao)
            )
            db.commit()
            # Redireciona para evitar reenvio do formulário
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            # Em caso de erro, pode-se adicionar uma mensagem de erro ao template
            print(f"Erro ao inserir livro: {e}")
            pass # Continua para listar os livros

    # Lógica para listar os livros (GET)
    cursor = db.cursor()
    cursor.execute("SELECT id, titulo, autor, ano_publicacao, disponivel FROM livros ORDER BY titulo")
    livros = cursor.fetchall()
    
    return render_template('index.html', livros=livros)


@app.route('/deletar/<int:livro_id>', methods=['POST'])
def deletar_livro(livro_id):
    db = get_db()
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        db.commit()
    except sqlite3.Error as e:
        print(f"Erro ao deletar livro: {e}")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # O caminho do banco de dados já está corrigido acima.
    app.run(host='0.0.0.0', port=5000, debug=True)
