import sqlite3 as sq

#criado by: vinicius(@v.ii.n.i)

def criarTable():
    """criando tabela"""
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()

        cur.execute('''CREATE TABLE teste(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL,
            telefone TEXT)''')

        con.commit()
    except Exception.__cause__ as erro:
        print(erro)
    finally:
        print('banco criado')
        cur.close()
        con.close()

def visualizarUser():
    """visualizando dados"""
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()

        cur.execute('''SELECT * FROM teste;''')
        for linha in cur.fetchall():
            print(linha)
        
        con.commit()
    except Exception.__cause__ as erro:
        print(erro)
    finally:
        cur.close()
        con.close()
    
def criarUser(nome, senha, telefone):
    """criando usuário"""
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()

        cur.execute('''INSERT INTO teste(nome, senha, telefone) VALUES("{}","{}","{}")'''.format(nome, senha, telefone))
        print("Usuário {} cadastrado".format(nome))
        con.commit()
    except Exception.__cause__ as erro:
        print(erro)
    finally:    
        cur.close()
        con.close()

def atualizarUser(nome, senha, telefone, id):
    """atualizar usuário"""
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()

        cur.execute('''UPDATE teste SET nome = "{}", senha = "{}", telefone = "{}" WHERE id = {}'''.format(nome, senha, telefone, id))

        print("Usuário {} atualizado".format(id))
        con.commit()
    except Exception.__cause__ as erro:
        print(erro)
    finally:    
        cur.close()
        con.close()

def deletarUser(id):
    """deletar usuário"""
    try:
        con = sq.connect('banco.db')
        cur = con.cursor()

        cur.execute('''DELETE FROM teste WHERE id = {}'''.format(id))

        print("Usuário {} deletado".format(id))
        con.commit()
    except Exception.__cause__ as erro:
        print(erro)
    finally:
        cur.close()
        con.close()