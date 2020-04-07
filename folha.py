#-*- coding:utf-8-*-
"""
Folha de Pagamento
Salário
Horas extras 100% (base 168h/mês)
Dependentes (cada dependente recebe 2% de salario)
INDICAR DESCONTOS E ADICIONAIS

Base de Cálculo (R$)	Alíquota (%)	Parcela a Deduzir do IR (R$)
De 6.677,56 a 9.922,28     7,5%	                 500,82
De 9.922,29 a 13.167,00	   15%	               1.244,99
De 13.167,01 a 16.380,38   22,5%	           2.232,51
Acima de 16.380,38	       27,5%	           3.051,53
"""
print("\n---FOLHA DE PAGAMENTO---")

Sair=False

while True:
    salario=(int(input("\nSalário Bruto:")))
    horas_extras=(int(input("Horas Extras:")))
    dependentes=(int(input("Dependentes:")))

    if salario>=6677.56 and salario<=9922.28:
        inss=salario*11/100
        irrf=salario*7.5/100
        dependentes=(salario*2/100)*dependentes
        horas_extras=(salario*0.60/100)*horas_extras
        liquido=salario-(inss+irrf)+horas_extras+dependentes

    if salario>=9922.29 and salario<=13167.00:
        inss=salario*11/100
        irrf=salario*15/100
        horas_extras=(salario*0.60/100)*horas_extras
        dependentes=(salario*2/100)*dependentes
        liquido=salario-(inss+irrf)+horas_extras+dependentes

    if salario>=13167.01 and salario<=16380.38:
        inss=salario*11/100
        irrf=salario*22.5/100
        horas_extras=(salario*0.60/100)*horas_extras
        dependentes=(salario*2/100)*dependentes
        liquido=salario-(inss+irrf)+horas_extras+dependentes

    if salario>16380.38:
        inss=salario*11/100
        irrf=salario*7.5/100
        horas_extras=(salario*0.60/100)*horas_extras
        dependentes=(salario*2/100)*dependentes
        liquido=salario-(inss+irrf)+horas_extras+dependentes

    print("Desconto INSS:", inss)
    print("Desconto IRRF:", irrf)
    print("Horas Extras:", horas_extras)
    print("Dependentes:", dependentes)
    print("Salário Líquido:", liquido)

    teste=input("\nDeseja sair:")
    if teste.lower()=="s":
    	break
