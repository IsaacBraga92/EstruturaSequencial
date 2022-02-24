# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
import math

cobertura_tinta = 6
capacidade_latao = 18
capacidade_galao = 3.6
preco_latao = 80.0
preco_galao = 25.0
latas_galao =0

tamanho_area = float(input("Informe o tamanho em metros quadrados da area a ser pintada: "))
area_folga = tamanho_area*1.1
litros = area_folga/cobertura_tinta
quant_latao = math.ceil(litros/capacidade_latao)
valor_latao = quant_latao*preco_latao
quant_galao = math.ceil(litros/capacidade_galao)
valor_galao = quant_galao*preco_galao

print("Latas grandes de 18L: ", quant_latao, "no valor de R$:", valor_latao)
print("Latas galão de 3.6L: ", quant_galao, "no valor de R$:", valor_galao)

#Compra otimizada

quant_latao = math.floor(litros/capacidade_latao)
valor_de_latao = quant_latao*preco_latao
litros_restantes = litros%capacidade_latao
quant_galao = math.ceil(litros_restantes/capacidade_galao)
valor_total = (quant_latao*preco_latao) + (quant_galao+preco_galao)

print("Você deverá usar", quant_latao,"de 18L e ", quant_galao,"de 3.6L, num valor total de: R$", valor_total)


