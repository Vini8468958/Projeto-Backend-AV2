# Notas Raphão: Necessário instalar o fastapi e uvicorn
# pip install fastapi | pip install uvicorn
# tive que atualizar o pip para conseguir instalar o fastapi, não sei se alguém mais teve esse problema, mas segue a linha de comando: python.exe -m pip install --upgrade pip
# Curiosidade: Quando um import não está sendo utilizado, ele fica "acinzentado"

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def get_db():
    conn = sqlite3.connect('biblioteca.db')
    conn.row_factory = sqlite3.Row
    return conn

# achava que aqui iria ficar conforme o banco de dados, mas não pode ter o id, já que isso poderia gerar conflitos na hora de criar novos livros

# id é gerado automaticamente pelo db

class Livro(BaseModel):
    # id: int
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool

# Essa parte aqui captura a lista de livros do banco de dados e retorna em formato JSON. Executando o Select e pegando todos os resultados com fetchall()m retorna em um dicionário, o que nos permite que a aplicação façça requisições HTTP para obter a lista de livros cadastrados no banco de dados.

@app.get("/livros")
def listar_livros():
    conn = get_db()
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return [dict(livro) for livro in livros]

# método get! (busca por id, por isso coloquei byid no nome)
@app.get("/livros/{id}")
def get_livroBy_id(id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
    livro = cursor.fetchone()
    conn.close()

    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return dict(livro)