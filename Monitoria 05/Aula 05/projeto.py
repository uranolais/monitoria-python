contatos = {}

def adicionar_contatos(nome, telefone):
    contatos[nome] = telefone

def exibir_contatos():
    print('Lista de contatos:')
    for nome,telefone in contatos.items():
        print(f'Nome:{nome}, Telefone: {telefone}')

adicionar_contatos('Mateus', 21315849)
adicionar_contatos('Lais',515662)
adicionar_contatos('Leticia',9865524)
exibir_contatos()

