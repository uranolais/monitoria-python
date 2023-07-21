# Cadastro de alunos usando listas
alunos_nomes = []
alunos_idades = []
alunos_notas = []

def cadastrar_aluno(nome, idade, nota):
    alunos_nomes.append(nome)
    alunos_idades.append(idade)
    alunos_notas.append(nota)

def exibir_alunos():
    for i in range(len(alunos_nomes)):
        print(f"Nome: {alunos_nomes[i]}, Idade: {alunos_idades[i]}, Nota: {alunos_notas[i]}")

# Teste do cadastro de alunos
cadastrar_aluno("João", 15, 9.5)
cadastrar_aluno("Maria", 16, 8.7)
exibir_alunos()

# Cadastro de alunos usando dicionários
alunos = {}

def cadastrar_aluno(nome, idade, nota):
    alunos[nome] = {'idade': idade, 'nota': nota}

def exibir_alunos():
    for nome, info in alunos.items():
        print(f"Nome: {nome}, Idade: {info['idade']}, Nota: {info['nota']}")

# Teste do cadastro de alunos
cadastrar_aluno("João", 15, 9.5)
cadastrar_aluno("Maria", 16, 8.7)
exibir_alunos()
