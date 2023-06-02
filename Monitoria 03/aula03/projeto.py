#menu -> if/else
#soma de numeros -> while/for

def soma_while():
    soma = 0
    numero = int(input("Digite um número: (digite 0 caso queira sair)"))
    while numero != 0:
        soma += numero
        numero = int(input("Digite um número: (digite 0 caso queira sair)"))
    print("A soma dos número digitados é:",soma)

def soma_for():
    soma = 0
    quantidade = int(input("Quantos números deseja somar?: "))
    for i in range(quantidade):
        numero = int(input("Digite um número: "))
        soma += numero
    print("A soma dos número digitados é:",soma)

def menu():
    print("Selecione uma opção:")
    print("1. Calcular a soma utilizando while")
    print("2. Calcular a soma utilizando for")
    print("0. Sair")

    opcao = int(input("Opção: "))
    if opcao == 1:
        soma_while()
    elif opcao == 2:
        soma_for()
    elif opcao == 0:
        print("Saindo :)")
    else:
        print("Opção não foi válida!")
        menu()

menu()
    
