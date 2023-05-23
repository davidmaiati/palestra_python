contador = 1
while(contador < 20):
    print(contador)
    contador = contador + 1
    if contador == 10:
        print("Início do bloco do if")
        print("Neste momento o contador vale 10")

        continue
        print("Fim do bloco if")

print("Linha após o bloco do while")
print("Fim do programa")
