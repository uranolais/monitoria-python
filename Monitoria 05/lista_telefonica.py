# Dicionário de contatos
contatos = {}

def adicionar_contato(nome, telefone):
    contatos[nome] = telefone

def exibir_contatos():
    print("Lista de Contatos:")
    for nome, telefone in contatos.items():
        print(f"Nome: {nome}, Telefone: {telefone}")

# Teste do dicionário de contatos
adicionar_contato("João", 123456789)
adicionar_contato("Maria", 987654321)
exibir_contatos()
