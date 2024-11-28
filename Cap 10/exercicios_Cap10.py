# 10.1 ============================================================================================

file_name = 'learning_python.txt'

# Lendo o arquivo todo
with open(file_name) as file_learning:
    conteudo = file_learning.read()
print(conteudo)

# Percorrendo o objeto arquivo com um laço
with open(file_name) as file_learning:
    for line in file_learning:
        print(line)

# a armazenando as linhas em uma lista
with open(file_name) as file_learning:
    lines = file_learning.readlines()
    for line in lines: print(line.strip())

# 10.2 ============================================================================================

file_name = 'learning_python.txt'

# Lendo o arquivo todo
with open(file_name) as file_learning:
    conteudo = file_learning.read()
    conteudo = conteudo.replace('Python', 'C#')

print(conteudo)

#10.3 ===========================================================================================

file_name = 'guest.txt'

with open(file_name, 'a') as guest_list:
    convidado = input("Digite seu nome: ")
    guest_list.write(convidado+'\n')

# 10.4 ================================================================================================

precisaMaisConvidados = True
guestBook_file = 'guest_book.txt'

with open(guestBook_file, 'a') as guestList:
    while(precisaMaisConvidados):
        print("Seja bem vindo(a) ao meu programa")
        nome = input('Digite seu nome para registrar sua passagem: ')
        guestList.write(nome+'\n')

        print("Nome registrado com sucesso!")
        maisConvidadosPergunta = input('Precisa registrar mais alguem? (S) (N): ')
        if maisConvidadosPergunta == 'S':
            continue
        else:
            break

# 10.5 ================================================================================================

precisaMaisRespostas = True
guestBook_file = 'gosta_programacao.txt'

with open(guestBook_file, 'a') as guestList:
    while(precisaMaisRespostas):
        print("Motivos para gostar de programação!")
        motivo = input('Digite um motivo: ')
        guestList.write(motivo+'\n')

        maisRespostasPergunta = input('Quer escrever mais algum motivo? (S) (N): ')
        if maisRespostasPergunta == 'S':
            continue
        else:
            break
# 10.6 – Adição:==================================================================================

try:
    val1 = int(input("Digite o primeiro número: "))
    val2 = int(input("Digite o segundo número: "))
    print(f'{val1} + {val2} = {val1 + val2}')
except ValueError:
    print("Ops, você não digitou valores válidos")

# 10.7 – Calculadora para adição::============================================
while True:
    try:
        val1 = int(input("Digite o primeiro número: "))
        val2 = int(input("Digite o segundo número: "))
        print(f'{val1} + {val2} = {val1 + val2}')
    except ValueError:
        print("Ops, você não digitou valores válidos")

# 10.8 – Gatos e cachorros:=================================================

files_names = ['dogs.txt', 'cats.txt', 'joaozinho.txt']

def imprimeArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as fl_obj:
        content = fl_obj.read()
        print(content)

for name in files_names: 
    try:
        imprimeArquivo(name)
        print("")
    except FileNotFoundError:
        print(f'{name} nao encontrado')

# 10.9 – Gatos e cachorros silenciosos:====================================

files_names = ['dogs.txt', 'cats.txt', 'joaozinho.txt']

def imprimeArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as fl_obj:
        content = fl_obj.read()
        print(content)

for name in files_names: 
    try:
        imprimeArquivo(name)
        print("")
    except FileNotFoundError:
        pass

# 10.10 – Palavras comuns: ==================================================

def contadorPalavras(nomeArquivo, palavra):
    with open(nomeArquivo, encoding = "utf-8") as file_object:
        content = file_object.read()
        words = content.split()
        count = 0

        for w in words:
            if w == palavra: count += 1
        
        print(f'A palavra "{palavra}" apareceu {count} vezes no arquivo {nomeArquivo}')

frank = 'frankenstein.txt'
moby = 'mobyDick.txt'
joao = 'joazinho.txt'

try:
    contadorPalavras(frank, 'the')
    contadorPalavras(moby, 'the')
    contadorPalavras(joao, 'the')
except FileNotFoundError:
    pass

# 10.11 – Número favorito: =================================================

import json

numFav = int(input("Digite seu numero favorito: "))

file_name = 'fav.json'

with open(file_name, 'w') as f_obj:
    json.dump(numFav, f_obj)

with open(file_name) as f_obj:
    number = json.load(f_obj)
    print(f'Seu numero favorito é {number}')