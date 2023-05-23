contador = 1
while(contador < 20):
    print(contador)
    if contador == 10:
        print("Início do bloco do if")
        print("Neste momento o contador vale 10")
        break
        print("Fim do bloco if")
    contador = contador + 1
print("Linha após o bloco do while")
print("Fim do programa")
