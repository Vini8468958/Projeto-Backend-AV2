# Notas Raphão: Necessário instalar o fastapi e uvicorn
# pip install fastapi | pip install uvicorn
# tive que atualizar o pip para conseguir instalar o fastapi, não sei se alguém mais teve esse problema, mas segue a linha de comando: python.exe -m pip install --upgrade pip
# Curiosidade: Quando um import não está sendo utilizado, ele fica "acinzentado"

from fastapi import FastAPI, HTTPException, status
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


# post
@app.post("/livros", status_code=status.HTTP_201_CREATED)
def criar_livro(livro: Livro):
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO livros (titulo, autor, ano_publicacao, disponivel)
            VALUES (?, ?, ?, ?)
            """,
            (livro.titulo, livro.autor, livro.ano_publicacao, int(livro.disponivel)),
        )
        conn.commit()

        novo_id = cursor.lastrowid
        cursor.execute("SELECT * FROM livros WHERE id = ?", (novo_id,))
        novo_livro = cursor.fetchone()
    except sqlite3.Error as e:
        conn.rollback()
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao criar livro: {str(e)}",
        )

    conn.close()
    return dict(novo_livro)


# put
@app.put("/livros/{id}")
def atualizar_livro(id: int, livro: Livro):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
    livro_existente = cursor.fetchone()

    if livro_existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    try:
        cursor.execute(
            """
            UPDATE livros
            SET titulo = ?, autor = ?, ano_publicacao = ?, disponivel = ?
            WHERE id = ?
            """,
            (
                livro.titulo,
                livro.autor,
                livro.ano_publicacao,
                int(livro.disponivel),
                id,
            ),
        )
        conn.commit()

        cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
        livro_atualizado = cursor.fetchone()
    except sqlite3.Error as e:
        conn.rollback()
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao atualizar livro: {str(e)}",
        )

    conn.close()
    return dict(livro_atualizado)


# delete
@app.delete("/livros/{id}")
def deletar_livro(id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE id = ?", (id,))
    livro_existente = cursor.fetchone()

    if livro_existente is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Livro não encontrado")

    try:
        cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        conn.close()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao deletar livro: {str(e)}",
        )

    conn.close()
    return {"mensagem": "Livro deletado com sucesso", "id": id}