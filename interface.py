#importando bibliotecas
import time
import bancoDB as bc
import os

#definindo variáveis
res = None

#limpa o terminal
os.system('clear')

#loop verdadeiro
print("\033[1;32m","conectando...","\033[m")
time.sleep(1.5)

#limpa o terminal
os.system('clear')

while True:
    res = None

    #--MENU--
    try:
        res = int(input('''
[0]VISUALIZAR
[1]CRIAR
[2]ATUALIZAR0
[3]DELETAR
[4]SAIR
RESPOSTA: '''))
    except:print("valor inválido")
    #ver usuários
    try:
        if res == 0:
            bc.visualizarUser()
            time.sleep(1.5)
        #criar usuário
        elif res == 1:
            nome = input("digite nome: ")
            senha = input("digite senha: ")
            telefone = input("digite um telefone: ")
            bc.criarUser(nome, senha, telefone)
            time.sleep(1.5)
        #atualizar usuário
        elif res == 2:
            nome = input("digite o nome: ")
            novoNome = input("digite o novo nome: ")
            senha = input("digite nova senha: ")
            telefone = input("digite novo telefone: ")
            
            bc.atualizarUser(nome, novoNome, senha, telefone)
            time.sleep(1.5)
        #deletar usuário
        elif res == 3:
            id = int(input("digite id: "))
            bc.deletarUser(id)
            time.sleep(1.5)
        #fechando o loop
        elif res == 4:
            #limpa o terminal
            os.system('clear')

            print("\033[1;31m","desconectando...","\033[m")
            time.sleep(1.5)
            #final do loop
            break
            
        #respota para número fora de [0-4]
        else: print("número inválido: \ntente novamente: ")

        #limpa o terminal depois de cada comando
        os.system('clear') or None
    except:os.system('clear') or None