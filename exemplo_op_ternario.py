'''
crie um programa que pergunte a idade ao usuário e em seguida informe se
este usuário é menor de idade ou maior de idade
'''

idade = int(input("Informe a sua idade:"))

resposta = ("menor de idade", ",aior de idade" )[idade >= 18]

print(f"Você é {resposta}")