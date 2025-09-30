# Peça um número e mostre o dobro, o triplo e a raiz quadrada.
numero = 25
dobro = numero * 2
tripo = numero * 3
for i in range(numero):
    if i * i == numero:
        raiz = i
        break
    else:
        print(f"{i} não e a raiz de {numero}")

print(f"""o dobro de {numero} e {dobro} o triplo e {tripo} e a raiz de {raiz}
       e {i}""")
