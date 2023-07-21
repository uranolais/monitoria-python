#LISTAS
alunos_nomes = []
alunos_idades = []
alunos_notas = []

def cadastrar_aluno(nome,idade,nota):
    alunos_nomes.append(nome)
    alunos_idades.append(idade)
    alunos_notas.append(nota)

def exibir_aluno():
    for i in range(len(alunos_nomes)):
        print(f'Nome:{alunos_nomes[i]},Idade:{alunos_idades[i]}, Nota: {alunos_notas[i]}')

cadastrar_aluno('Mateus',21,10)
cadastrar_aluno('Lais',51,4)
cadastrar_aluno('Leticia',9,9)
exibir_aluno()

# Dicionário
alunos = {}

def cadastrar_alunos(nome,idade,nota):
    alunos[nome] = {'idade': idade, 'notas':nota}

def exibir_alunos():
    for nome, informacoes in alunos.items():
        print(f"Nome: {nome}, Idade: {informacoes['idade']}, Notas: {informacoes['notas']}")

cadastrar_alunos('Mateus',21,10)
cadastrar_alunos('Lais',51,4)
cadastrar_alunos('Leticia',9,9)
exibir_alunos()



