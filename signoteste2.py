#-*- coding:utf-8-*-
"""
Signos
Autor: Paloma
Função: descubrir o signo
"""
print ("\n*----Signos----*\n")
print("Data de Nascimento")

Sair=False

while True:
	dia=input("Digite dia:")
	dia=int(dia)
	mes=input("Digite mês:")
	mes=int(mes)
	
	while (dia<=0 or  dia>31 ) or  (mes<=0 or mes>12):
		print("------------ Parametros invalidos-----------")
		dia=int( input("Data invalida") )
		mes=int(input('Data invalida. Digite mes entre 1 e 12 : ') )
		

	if dia <=22 and mes==12 or dia<=21 and mes==1:
		signo="Capricórino"

	if dia>=22 and mes==1 or dia<=21 and mes==2:
		signo="Aquário"

	if dia>=22 and mes==2 or dia<=21 and mes==3:
		signo="Peixes"

	if dia>=22 and mes==3 or dia<=21 and mes==4:
		signo="Aries"

	if dia>=22 and mes==4 or dia<=21 and mes==5:
		signo="Touro"

	if dia>=22 and mes==5 or dia<=21 and mes==6:
		signo="Gêmeos"

	if dia>=22 and mes==6 or dia<=21 and mes==7:
		signo="Câncer"

	if dia>=22 and mes==7 or dia<=21 and mes==8:
		signo="Leão"

	if dia>=22 and mes==8 or dia<=21 and mes==9:
		signo="Virgem"

	if dia>=22 and mes==9 or dia<=21 and mes==10:
		signo="Libra"

	if dia>=22 and mes==10 or dia<=21 and mes==11:
		signo="Escorpião"

	if dia>=22 and mes==11 or dia<=21 and mes==12:
		signo="Sargitário"	

	print("O Signo é:", signo) 
	

	teste=input("Deseja sair:")
	if teste.lower()=='s':
		break
		