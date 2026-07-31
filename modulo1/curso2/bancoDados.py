import sqlite3
from pathlib import Path

ROOTH_PATH = Path(__file__).parent


conexao = sqlite3.connect(ROOTH_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(cursor, conexao):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))"
    )
    conexao.commit()


# Create
def inserir_registro(cursor, conexao, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


# Read
def ler_registro(cursor, id):
    data = (id,)
    cursor.execute("SELECT * FROM clientes WHERE id =?;", data)
    return cursor.fetchone()


def ler_varios_registro(cursor):
    return cursor.execute("SELECT nome, email, id FROM clientes;")


# Update
def atualizar_registro(cursor, conexao, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id  = ?;", data)
    conexao.commit()


# Delete
def deletar_registro(cursor, conexao, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id =?;", data)
    conexao.commit()


def criar_varios(cursor, conexao, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()


"""criar_tabela(cursor, conexao)
inserir_registro(cursor, conexao, "Samuel", "samuel@email.com")
atualizar_registro(cursor, conexao, "Samuel Campelo", "samuel@email.com", 1)

inserir_registro(cursor, conexao, "Lara", "lara@email.com")
deletar_registro(cursor, conexao, 2)

dados = {
    ("bete", "bete@email.com"),
    ("laraLinda", "lara@email.com"),
    ("suzana", "suzana@email.com"),
    ("moises", "moises@email.com"),
}
criar_varios(cursor, conexao, dados)"""

cliente = ler_registro(cursor, 4)
print(dict(cliente))

print(f'ola cliente {cliente["nome"]}')

clientes = ler_varios_registro(cursor)
for cliente in clientes:
    dict(cliente)
    print(cliente["nome"] + " = " + cliente["email"])


try:
    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?,?);",
        ("zildidar", "zildinar@email.com"),
    )
    cursor.execute(
        "INSERT INTO clientes (id, nome, email) VALUES (?,?,?);",
        (5, "zildidar", "zildinar@email.com"),
    )
    conexao.commit()
except Exception as exc:
    print(f"ops, deu b.o! {exc}")
    conexao.rollback()
