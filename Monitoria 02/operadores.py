# Operadores Aritméticos
a = 10 #atribuição
b = 3

soma = a + b #3
subtracao = a - b #7
multiplicacao = a * b #30
divisao = a / b #3.335
divisao_inteira = a // b #3
resto = a % b #1
exponencial = a**b #1000

# print(soma,subtracao,multiplicacao,divisao,divisao_inteira,resto,exponencial)
# print('A soma de {} com {} é: {}'.format(a,b,soma))
# print(f'A soma de {a} com {b} é: {soma}')

#Operadores de Atribuição
c = 5
d = 2

c += d #Equivalente à c = c + d #7
c -= d #Equivalente à c = c - d #5
c *= d #Equivalente à c = c * d #10
c /= d #Equivalente à c = c / d #5.0
c //= d #Equivalente à c = c // d #2
c %= d #Equivalente à c = c % d #0
c **= d #Equivalente à c = c ** d #0

#Operadores de Comparação

e = 5
f = 3

igual = e == f       # False
diferente = e != f   # True
maior_que = e > f    # True
maior_ou_igual = e >= f   # True
menor_que = e < f    # False
menor_ou_igual = e <= f   # False

#Operadores Lógicos

g = True
h = False

e_logico = g and h    # False - Basta um ser falso (2v)
ou_logico = g or h    # True - Basta um ser verdadeiro
nao_logico = not g    # False - O contrário