# Criando dicionário
dicionario = {}
dicionario_dois = dict()

# Inserindo elementos
dicionario['chave1'] = 'valor1'
dicionario[1] = 234
dicionario[2.3] = 'valor3'
dicionario['lista'] = [1,2,3,4]
print(dicionario['lista']) # ir alterando esses valores

# Deletando todos os valores
dicionario.clear()

# Inserindo de outras maneiras

dicionario = {'chave1':'valor1','chave2':'valor2'}
tamanho = len(dicionario)
print(tamanho)
valor = dicionario.get('chaves1','chave não existe')
print(valor)
chaves = dicionario.keys()
print(chaves)
valores = dicionario.values()
print(valores)
itens = dicionario.items()
print(itens)
valor = dicionario.pop('chave1')
print(valor)
valor = dicionario.pop('chaves1',None)
print(valor)
dicionario.update({'chave3': 'valor3'})
print(dicionario)

# Lista Telefonica

contatos = {}

def adicionar_contato(nome,telefone):
    contatos[nome] = telefone

def exibir_contatos():
    print('Lista de contatos: ')
    for nome, telefone in contatos.items():
        print(f'Nome: {nome}, Telefone: {telefone}')

adicionar_contato('Lais',123654789)
adicionar_contato('Joao',415265622)
exibir_contatos()














