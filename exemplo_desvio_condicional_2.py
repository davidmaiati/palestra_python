'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

numero = int(input("Informe um número"))

if(numero % 2 == 0):
    print("Esse número é par")
else:
    print("Esse número é ímpar")