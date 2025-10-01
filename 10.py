"""
Calcule quanto tempo demora para percorrer uma
distância a partir da velocidade média
"""
"""
a formula e tempo = distancia / velocidade
"""
"""
para saber o tempo e distancia / por velocidade o tempo eo resultado dessa
divisão para poder saber quantos minutos e tem que pegar aa hora transformar
em inteiro assim vai pegar a hora subtrair menos o tempo, para conseguir pegar
o resto da divisão e para saber quantos minutos ee so multiplicar por 60
que ai terar o resultado de quantos minutos são
"""
distanci = float(input("insira a distancia que deseja percorrer, em km: "))
velocidade = int(input("insira a velocidade media: "))
tempo = distanci / velocidade
hora = int(tempo)
minutos = (tempo - hora)*60
print(f"o tempo medio de chegada e {hora:.0f} horas e {minutos:.0f} minutos")

"""
Calcule quanto tempo demora para percorrer uma
distância a partir da velocidade média.
d = 15
v = 10
tp_t = d / v
h = int(tp_t)
m = (tp_t - h) * 60 #colocar tempo total na frente de hora por que tempo total
sempre vai ser maior que hora
print(f"o tempo medio e {h:.0f} horas e {m:.0f} minutos")
"""
