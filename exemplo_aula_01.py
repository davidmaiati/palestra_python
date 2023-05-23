'''
Perguntar nome, idade e salário da pessoa;
Em seguida exibir estes dados
'''

nome = input("Informe seu nome?")
print(f"Olá", {nome}, "tudo bem com você?")
print("var nome", type(nome))

idade = int(input("Qual sua idade?"))
print(f"Nossa, você tem", {idade}, "anos?" )
print("var idade", type(idade))

salario = float(input("Qual salário pretendido?"))
print(f"Seu salário é {salario:.2f}")
print("var salário", type(salario))

