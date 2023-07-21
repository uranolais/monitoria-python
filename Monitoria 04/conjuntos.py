#LISTA
lista = [0,1,2,3]
type(lista) #<class 'list'>
lista[0] #0
lista.append(4) #[0, 1, 2, 3, 4]
lista.pop() #4
del lista[1:3] #[0, 3]
lista.clear() #[]
lista = [0,1,2,3]
len(lista) #4
lista[1] = 5 #[0, 5, 2, 3]
del lista[1] #[0, 2, 3]
lista[1] #2
lista.insert(1,1) #[0, 1, 2, 3]

# #TUPLA
# tupla = (0,1,2,3,4)
# type(tupla) #<class 'tuple'>
# tupla[1] #1
# tupla.pop()
# '''Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'pop'''
# tupla.append(5)
# '''Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'''

# # Procurando um valor em uma lista
# lista_frutas = ['maçã', 'banana', 'laranja']
# fruta = 'banana'

# if fruta in lista_frutas:
#     print(fruta, "encontrada na lista!")
# else:
#     print(fruta, "não encontrada na lista.")

# # Procurando um valor em uma tupla
# tupla_cores = ('vermelho', 'verde', 'azul')
# cor = 'amarelo'

# if cor in tupla_cores:
#     print(cor, "encontrada na tupla!")
# else:
#     print(cor, "não encontrada na tupla.")
