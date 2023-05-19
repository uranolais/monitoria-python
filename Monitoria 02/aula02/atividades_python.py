# Atividade 01: Verificação de idade
idade = 18 #Exemplo, teste outros valores

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Atividade 02: Verificação de valores
numero = -3.5 #Exemplo, teste outros valores

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Atividade 03: Verifique se o número é par ou impar
numero = 3

if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é impar.')

# Atividade 04: Cálculo de média ponderada
nota1 = 7.3
peso1 = 2
nota2 = 8.4
peso2 = 5
nota3 = 6.2
peso3 = 3

media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print("Média ponderada:", media_ponderada)

# Atividade 05: Cálculo e verificação de categorias

valor1 = 56
valor2 = 1.6

resultado = valor1 / valor2 ** 2

if resultado < 18.5:
    print("Categoria A.")
elif 18.5 <= resultado < 25:
    print("Categoria B.")
elif 25 <= resultado < 30:
    print("Categoria C.")
else:
    print("Categoria D.")