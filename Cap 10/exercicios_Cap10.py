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