'''
crie um programa que pergunte a idade ao usuário e em seguida informe se
este usuário é menor de idade ou maior de idade
'''

idade = int(input("Informe a sua idade:"))

resposta = ("maior de idade" if idade >= 18 else "menor de idade")

print(f"Você é {resposta}")