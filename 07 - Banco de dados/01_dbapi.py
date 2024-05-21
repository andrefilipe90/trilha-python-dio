import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "teste.sqlite")
cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150)"
    )
    conexao.commit()


def adicionar_valores(conexao, cursor, nome, email):
    info = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", info)
    conexao.commit()


def alterar_valores(conexao, cursor, id, nome, email):
    info = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? where id=?;", info)
    conexao.commit()


def remover_valores(conexao, cursor, id):
    info = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", info)
    conexao.commit()


def adicionar_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    conexao.commit()


dados = [
    ("André", "andre@gmail.com"),
    ("Sophie mattos", "Sophiemattos@gmail.com"),
    ("Denise", "denise@gmail.com"),
    ("Marielle", "marielle@gmail.com"),
]

adicionar_muitos(conexao, cursor, dados)
# remover_valores(conexao, cursor, 2)
# alterar_valores(conexao, cursor, 1, "André Mattos", "andrefilipe90@gmail.com")
# def criar_tabela(conexao, cursor):
#     cursor.execute(
#         "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
#     )
#     conexao.commit()


# def inserir_registro(conexao, cursor, nome, email):
#     data = (nome, email)
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
#     conexao.commit()


# def atualizar_registro(conexao, cursor, nome, email, id):
#     data = (nome, email, id)
#     cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
#     conexao.commit()


# def excluir_registro(conexao, cursor, id):
#     data = (id,)
#     cursor.execute("DELETE FROM clientes WHERE id=?;", data)
#     conexao.commit()


# def inserir_muitos(conexao, cursor, dados):
#     cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
#     conexao.commit()


# def recuperar_cliente(cursor, id):
#     cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
#     return cursor.fetchone()


# def listar_clientes(cursor):
#     return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(dict(cliente))

# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))
# print(cliente["id"], cliente["nome"], cliente["email"])
# print(f'Seja bem vindo ao sistema {cliente["nome"]}')

# # dados = [
# #     ("Guilherme", "guilherme@gmail.com"),
# #     ("Chappie", "chappie@gmail.com"),
# #     ("Melaine", "melaine@gmail.com"),
# # ]
# # inserir_muitos(conexao, cursor, dados)
