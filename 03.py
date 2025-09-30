# Solicite dois números e mostre a média.

numero1 = int(input(" insira um numero:"))
numero2 = int(input(" insira um segundo numero: "))

# vou criar uma condiçao para somar sempre o numero maior
"""dessa maneira tem mais repetição de codigo, caso eu dejese
 mudar alguma coisa tenhoque mudar em dois lugares"""

if numero1 >= numero2:
    print(f"a media dos numeros e {numero1/numero2:.0f}")
else:
    print(f"a media dos numeros e {numero2/numero1:.0f}")

# posso fazer de outra maneira tambem
"""dessa meneira e mais otimizado, uso variaveis e eu posso usar o soma para
manipular depois, mais codigo mas mais otimizado"""

if numero1 >= numero2:
    soma = numero1 / numero2
else:
    soma = numero2 / numero1
print(f"a media e {soma:.2f}")

# tem de outra maneira tambem
"""dessa maneira e mais otimizado ainda, usando metodos max e min,
 otimizado e menos codigo, mais legivel"""

resultado = max(numero1, numero2) / min(numero1, numero2)
print(f"o resultado e {resultado:.2f}")
