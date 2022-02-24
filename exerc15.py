#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

salarioHora = float(input("Informe o seu salario por hora: "))
horasMensal = int(input("Informe a quantidade de horas trabalhadas no mês: "))

salarioTotalBruto = salarioHora*horasMensal
impostoRenda = salarioTotalBruto*0.11
inss = salarioTotalBruto*0.08
sindicado = salarioTotalBruto*0.05
salarioliquido = salarioTotalBruto-impostoRenda-inss-sindicado
print("O salario liquido mensal é: ", salarioliquido)