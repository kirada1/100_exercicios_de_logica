# Solicite o salário e calcule um aumento de 15%.

salario = float(input("insira o valor do seu salario: "))
aumento = 15
porcentagem = (salario * aumento) / 100
"""
uso o replace pata substituir o , do da casa decial de milhar
quandoe eu coloc :, ele formata a casa de milhar com o padrao americano
que e , eo repalce estou pegando o , e trocando pata .
"""
print(
    (
      f"seu aumento foi de {aumento}% equivalente a "
      f"{porcentagem:,} e seu novo salario"
      f" e {salario + porcentagem:,}"
    ).replace(",", ".")
)
