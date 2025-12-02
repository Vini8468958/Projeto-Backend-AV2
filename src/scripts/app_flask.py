import sqlite3
from flask import Flask, render_template, request, redirect, url_for, g

# Configuração
DATABASE = 'biblioteca.db'
app = Flask(__name__)
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

if __name__ == '__main__':
    # Garante que o banco de dados está no diretório correto
    import os
    os.chdir('/home/ubuntu/app_flask_project')
    app.run(host='0.0.0.0', port=5000, debug=True)
