# Criando um dicionário vazio
meu_dicionario = {}
outro_dicionario = dict()
# Inicializando um dicionário com valores
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
tamanho = len(meu_dicionario)  # tamanho = 2
valor = meu_dicionario.get('chave1')  # valor = 'valor1'
print(valor)
valor = meu_dicionario.get('chave3', 'Valor padrão')  # valor = 'Valor padrão'
print(valor)
chaves = meu_dicionario.keys()    # chaves = dict_keys(['chave1', 'chave2'])
print(chaves)
valores = meu_dicionario.values() # valores = dict_values(['valor1', 'valor2'])
print(valores)
itens = meu_dicionario.items()    # itens = dict_items([('chave1', 'valor1'), ('chave2', 'valor2')])
print(itens)
valor = meu_dicionario.pop('chave1')         # valor = 'valor1', dicionário fica {'chave2': 'valor2'}
valor = meu_dicionario.pop('chave3', None)   # valor = None, chave3 não existe, dicionário não é modificado
meu_dicionario.update({'chave3': 'valor3', 'chave4': 'valor4'})
# Resultado: {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
meu_dicionario.clear()  # Resultado: {}

