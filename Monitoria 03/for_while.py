# Utilizando a estrutura de repetição "while"
def soma_while():
    soma = 0
    numero = int(input("Digite um número (0 para sair): "))
    
    while numero != 0:
        soma += numero
        numero = int(input("Digite um número (0 para sair): "))
    
    print("A soma dos números digitados é:", soma)


# Utilizando a estrutura de repetição "for"
def soma_for():
    soma = 0
    quantidade = int(input("Quantos números deseja somar? "))#3
    
    for i in range(quantidade):
        numero = int(input("Digite um número: "))
        soma += numero
    
    print("A soma dos números digitados é:", soma)


# Menu principal
def menu():
    print("Selecione uma opção:")
    print("1. Calcular soma utilizando while")
    print("2. Calcular soma utilizando for")
    print("0. Sair")
    
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        soma_while()
    elif opcao == 2:
        soma_for()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
        menu()


# Execução do programa
menu()

