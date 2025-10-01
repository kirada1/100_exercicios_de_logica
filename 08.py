import math
# Peça um número e mostre o dobro, o triplo e a raiz quadrada.
numero = 24
dobro = numero * 2
tripo = numero * 3
for i in range(numero):
    if i * i == numero:
        raiz = i
        print(f"{i} ea raiz de {raiz}")
        break
    else:
        print(f"{numero} não e uma raiz quadrada")
        break

# outra maneira de resolver
for i in range(numero):
    if i * i == numero:
        raiz_quadrada = math.sqrt(numero)
        print(f"a raiz quadrada de {numero} e {raiz_quadrada}")
        break
    else:
        print(f"{numero} não tem raiz quadrada")
        break
