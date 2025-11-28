import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[1] / "data" / "biblioteca.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER,
    disponivel INTEGER NOT NULL DEFAULT 1
)
""")

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

conn.commit()
conn.close()

print("Banco criado/atualizado em:", DB_PATH)
