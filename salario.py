#-*- coding:utf-8-*-
"""
Salários
Indicar salário bruto
Indicar desconto INSS
Indicar salário líquido

ALIQUOTA INSS
até 1.830,29 8%
de 1.830,30 a 3.050,52 9%
de 3.050,53 a 6.101,06 11%
"""

print("\n-----Salário-----")

Sair=False

while True:
	salario=input("\nSalário Bruto:")
	salario=float(salario)


	if salario<=1830.29:
		inss=salario*8/100
		liquido=salario-inss

	if salario>=1830.30 and salario<=3050.52:
		inss=salario*9/100
		liquido=salario-inss

	if salario>=3050.53 and salario<=6101.06:
		inss=salario*11/100
		liquido=salario-inss

	print("Valor pago de INSS:",inss)
	print("Valor líquido:",liquido)

	teste=input("\nDeseja sair:")
	if teste.lower()=="s":
		break
