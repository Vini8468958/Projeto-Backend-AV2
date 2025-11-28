from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).resolve().parent / "src" / "data" / "biblioteca.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route("/", methods=["GET"])
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, titulo, autor, ano_publicacao, disponivel FROM livros ORDER BY id")
    livros = cur.fetchall()
    conn.close()
    return render_template("index.html", livros=livros)

@app.route("/add", methods=["POST"])
def add():
    titulo = request.form.get("titulo", "").strip()
    autor = request.form.get("autor", "").strip()
    ano = request.form.get("ano_publicacao") or None
    disponivel = 1 if request.form.get("disponivel") == "on" else 0

    if not titulo or not autor:
        return redirect(url_for("index"))

    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO livros (titulo, autor, ano_publicacao, disponivel) VALUES (?, ?, ?, ?)",
        (titulo, autor, ano if ano != "" else None, disponivel)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
