# -> Aqui é feita a importação do sqlite e do modulo path 
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "biblioteca.db" #-> linha que monta automaticamente o caminho ate arquivo biblioteca. 
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

#-> É aberto a conexão com o banco de dados e criado o cursor
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# -> nesse bloco é executado a crição da tabela livros 
cur.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER,
    disponivel INTEGER NOT NULL DEFAULT 1
)
""")

# -> aqui é verificado se a tabela esta vazia 
cur.execute("SELECT COUNT(1) FROM livros")
count = cur.fetchone()[0]


if count == 0:  
    cur.executemany("""
    INSERT INTO livros (titulo, autor, ano_publicacao, disponivel)
    VALUES (?, ?, ?, ?)
    """, [
        ("Dom Casmurro", "Machado de Assis", 1899, 1),
        ("A Moreninha", "Joaquim Manuel de Macedo", 1844, 1),
        ("O Alienista", "Machado de Assis", 1882, 0)
    ])

# -> aqui eu faço commit da aletrações e fecho a conexão do banco de dados 
conn.commit()
conn.close()

print("Banco criado/atualizado em:", DB_PATH)
