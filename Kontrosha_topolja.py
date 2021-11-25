#n=''
#while n not in [1,2,3,4,5,6,7,8,9]:
#	try:
#		n=int(input('Сколько домов построить (от 1 до 9): '))
#	except ValueError:
#		print('Введите одно число от 1 до 9')
#for i in range(n):
#	print(' ~~~~~ ',end=(' '))
#print()
#for i in range(n):
#	print('/_____\ ',end=(''))
#print()
#for i in range(n):
#	print('| []  |',end=(' '))
#print()
#for i in range(n):
#	print(' ----- ',end=(' '))


#from random import *
#summaOcenok=0
#kolvoUchenikov=randint(15,30)
#for i in range(kolvoUchenikov):
#	ocenka=randint(1,5)
#	if ocenka<5:
#		ocenka=ocenka+round(random(),2)
#	summaOcenok+=ocenka
#print('средняя оценка в А классе - ', round(summaOcenok/kolvoUchenikov,2))
#summaOcenok=0
#for i in range(kolvoUchenikov):
#	ocenka=randint(2,5)
#	summaOcenok+=ocenka
#print('средняя оценка в Б классе - ', round(summaOcenok/kolvoUchenikov,2))


#from random import *

#maxOcenka=0
#minOcenka=5
#kolvoUchenikov=randint(30,60)
#for i in range(kolvoUchenikov):
#	ocenka=randint(1,5)
#	if ocenka<5:
#		ocenka=ocenka+random()
#		ocenka=round(ocenka,2)
#	print(ocenka, end=', ')
#	if ocenka>maxOcenka:
#		maxOcenka=ocenka
#	if ocenka<minOcenka:
#		minOcenka=ocenka
#print()
#print('Минимальная оценка - ',minOcenka)
#print('Максимальная оценка - ',maxOcenka)


#from random import *
#plotnostOblasti=0
#for i in range(12):
#	kolvoLudej=randint(1000,10000)
#	plosad=randint(1,15)
#	plotnostOblasti+=kolvoLudej/plosad
#print('Среднюю плотность населения по области в целом равна - ',round(plotnostOblasti/12,0))


#x=''
#maxX=''
#stepX=''
#n=0
#while type (x)!=int:
#	try:
#		x=int(input('Введи минимальный X: '))
#	except ValueError:
#		print('Введи целое число')
#while type (maxX)!=int:
#	try:
#		maxX=int(input('Введи максимальный X: '))
#	except ValueError:
#		print('Введи целое число')
#while type (stepX)!=int:
#	try:
#		stepX=int(input('Введи шаг для изменения X: '))
#	except ValueError:
#		print('Введи целое число')
#while x<maxX:
#	n+=1
#	x+=stepX
#	print(f'X{n} равен: {x}')
#	y=round(-0.5*x+x,2)
#	print(f'Y{n} равен: {y}')