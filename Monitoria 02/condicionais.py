#!/usr/bin/env python3

"""Cor Favorita

Com base na cor favorita do usuário, o script exibirá uma mensagem correspondente.

Uso:
    python3 cor_favorita.py
"""

cor = input("Qual é a sua cor favorita? ")

mensagem = "Essa é uma cor legal!"


"""
if cor == "azul":
    mensagem = "Ótima escolha! Azul é uma cor tranquilizante."
    
elif cor == "vermelho":
    mensagem = "Legal! Vermelho é uma cor energética e apaixonada."
    
elif cor == "amarelo":
    mensagem = "Incrível! Amarelo é uma cor brilhante e alegre."
    
elif cor == "verde":
    mensagem = "Legal! Verde está associado à natureza e à frescura."
    
elif cor == "roxo":
    mensagem = "Adorável! Roxo muitas vezes está ligado à criatividade e realeza."
    
else:
    mensagem = "Não conheço essa cor, mas deve ser ótima!"
"""

match cor:
    case "azul":
        mensagem = "Ótima escolha! Azul é uma cor tranquilizante."
    case "vermelho":
        mensagem = "Legal! Vermelho é uma cor energética e apaixonada."
    case "amarelo":
        mensagem = "Incrível! Amarelo é uma cor brilhante e alegre."
    case "verde":
        mensagem = "Legal! Verde está associado à natureza e à frescura."
    case "roxo":
        mensagem = "Adorável! Roxo muitas vezes está ligado à criatividade e realeza."
    case other:
        mensagem = "Não conheço essa cor, mas deve ser ótima!"
    

print(mensagem)