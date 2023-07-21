dicionario = {}
dicionario_dois = dict()

dicionario['chave1'] = 'valor1'
dicionario[1] = [1,2,1]
dicionario[2.4] = 'c'
dicionario.clear()

dicionario = {'chave1':'valor1','chave2':'valor2'}
# print(dicionario)
tamanho = len(dicionario)
# print(tamanho)
valor = dicionario.get('chave1','chave não encontrada')
# print(valor)
chaves = dicionario.keys()
valores = dicionario.values()
# print(chaves)
# print(valores)
itens = dicionario.items()
# print(itens)
v = dicionario.pop('chave1', None)
print(v)
print(dicionario)
dicionario.update({'chave2':'valor3'})
print(dicionario)