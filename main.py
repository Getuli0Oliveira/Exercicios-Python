# Loop simples com while

x = 1
while (x < 6):
  print(x)
  x = x + 1
  
# Loop while com if

inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))
x = inicial

while (x <= final):
	if (x % 2 == 0):
		print(x)
	x = x + 1 
  
 # Acumulador

soma = 0 
cont = 1 

while (cont <= 5):
	x = float(input('Digite a {}ª nota'.format(cont)))
	soma = soma + x
	cont = cont + 1 
media = soma / 5
print('Média final: {}'.format(media))


Operadores especiais de atribuição
------------------------------------
# OPERADOR | EXEMPLO | EQUIVALENTE -
#   +=	     x += 1     x = x + 1  -
#   -=       x -= 1     x = x - 1  -
#   *=       x *= 1     x = x * 1  -
#   /=	     x /= 2     x = x / 2  -
#   **=      x **=2     x = x **2  -
#   //=      x //=4     x = x //4  -
------------------------------------

soma = 0 
cont = 1 

while (cont <= 5):
	x = float(input('Digite a {}ª nota'.format(cont)))
	soma += x
	cont += 1  
media = soma / 5
print('Média final: {}'.format(media))

# Validando dados de entrada

x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
	x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...'.format(x))	

# Instrução break

print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar digite "sair".')
while True: 
	texto = input('')
	print(texto)
	if texto == 'sair': 
		break
print('Encerrando o programa...')

# Instrução continue

# Caso a condição permaneça True, o programa utiliza o continue para voltar ao início do loop. Assim que passa de True para False, o programa continua
# a verificar e passa para a próxima condição, que então pede a senha ao user. Caso a senha esteja incorreta, a função break encerra o programa. 

while True: 
	nome = input('Qual o seu nome?')
	if (nome != 'Getúlio'):
		continue
	senha = input('Qual a sua senha?')
	if(senha == 'GeTuLiO'):
		break
print('Acesso concedido')

# Valores Truthy e Falsey

nome = ''
while not nome: 
	nome = input('Digite seu nome:')
valor = int(input('Digite um número qualquer: '))
if valor:
	print('Você digitou um valor diferente de zero.')
else:
	print('Você digitou zero')
	
# Estrutura de repetição for

for i in range (50): 
	print(i)
	
# 1º Número valor inicial, 2º Valor final e 3º Intervalo de contagem (de 1 em 1, de 2 em 2 etc...)	

for i in range (1, 50, 5): 
	print(i)

# O mesmo pode ser feito para contar regressivamente	

for i in range (10,0,-2)	

# Comparativo while e for

x = 1 

while (x<6):
	print(x)
	x = + 1

--	
	
for i in range (1,6,1):
	print(i)
	
# Exercício

soma = 0
qtd = 0 
for i in range(1,101):
	if (i % 2 == 0):
		soma += i
		qtd += i
media = soma / qtd 
print('A média dos pares de 1 até 100 é: {}'.format(media))

# Estruturas de repetição aninhadas

# Calculo de tabuada com 2 while

tabuada = 1 
while tabuada <= 10: 
	print('Tabuada do {}'.format(tabuada))
	i = 1
	while i<= 10:
		print('{} x {} = {}'.format(tabuada, i, tabuada * i))
		i += 1
	tabuada += 1
	
# 2 for
	
	for tabuada in range (1,11,1):
	print('Tabuada do {}'.format(tabuada))
	for i in range (1,11,1):
		print('{} x {} = {}'.format(tabuada, i, tabuada * i))
		
# while e for

tabuada = 1 
while tabuada <= 10: 
	print('Tabuada do {}'.format(tabuada))
	for  i in range (1,11,1): 
		print('{} x {} = {}'.format(tabuada, i, tabuada * i))
	tabuada+= 1 

	
# Exercícios de fixação estruturas de repetição 

for i in range (3,13):
	print(i)

i = 3
while (i<13):
	print(i)
	i +=1

---

for i in range (0,9,2):
	print(i)
	
	i = 0
while (i < 9):
	print(i)
	i +=1
---	

Calculadora

print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite "Sair para encerrar o programa"')

op = input('Qual operação deseja fazer? ')

if op == '+' or op == '-' or op == '*' or op == '/':
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: '))

if (op == '+'):
	res = x + y 
	print('Resultado: {} + {} = {}'.format(x, y, res))
elif (op == '-'):
	res = x - y 
	print('Resultado: {} - {} = {}'.format(x, y, res))
elif (op == '*'):
	res = x * y 
	print('Resultado: {} * {} = {}'.format(x, y, res))
elif (op == '/'):
	res = x / y 
	print('Resultado: {} / {} = {}'.format(x, y, res))
else:
	print('Operaçao inválida')
	
	
Calculadora com laço de repetição 	
	
	
print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite "Sair para encerrar o programa"')

op = input('Qual operação deseja fazer? ')


if op == '+' or op == '-' or op == '*' or op == '/':
	x = int(input('Digite o primeiro valor: '))
	y = int(input('Digite o segundo valor: '))

while (op != 's'):	
	if (op == '+'):
		res = x + y 
		print('Resultado: {} + {} = {}'.format(x, y, res))
	elif (op == '-'):
		res = x - y 
		print('Resultado: {} - {} = {}'.format(x, y, res))
	elif (op == '*'):
		res = x * y 
		print('Resultado: {} * {} = {}'.format(x, y, res))
	elif (op == '/'):
		res = x / y 
		print('Resultado: {} / {} = {}'.format(x, y, res))
	else:
		print('Operaçao inválida')
	
	op = input('Qual operação deseja fazer? ')
	if op == '+' or op == '-' or op == '*' or op == '/':
		x = int(input('Digite o primeiro valor: '))
		y = int(input('Digite o segundo valor: '))
			
print('Encerrando o programa...')		


Calculadora com laço de repetição usando break and continue

print('Calculadora')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Digite "Sair para encerrar o programa"')



while True:
	op = input('Qual operação deseja fazer? ')
	if op == '+' or op == '-' or op == '*' or op == '/':
		x = int(input('Digite o primeiro valor: '))
		y = int(input('Digite o segundo valor: '))
	
	if (op == '+'):
		res = x + y 
		print('Resultado: {} + {} = {}'.format(x, y, res))
		continue
	elif (op == '-'):
		res = x - y 
		print('Resultado: {} - {} = {}'.format(x, y, res))
		continue
	elif (op == '*'):
		res = x * y 
		print('Resultado: {} * {} = {}'.format(x, y, res))
		continue
	elif (op == '/'):
		res = x / y 
		print('Resultado: {} / {} = {}'.format(x, y, res))
		continue
	elif (op== 's'):
		break
	else:
		print('Operaçao inválida')	
			
print('Encerrando o programa...')	

Calculadora de cédulas utilizado IFs somente: 
	
valor = int(input('Digite o valor em R$ '))

if valor >= 100:
	cedulas100 = valor // 100
	valor -= cedulas100 * 100
	print('Cédulas de 100: {}'.format(cedulas100))
if valor >= 50:
	cedulas50 = valor // 50
	valor -= cedulas50 * 50
	print('Cédulas de 50: {}'.format(cedulas50))
if valor >= 20:
	cedulas20 = valor // 20
	valor -= cedulas20 * 20
	print('Cédulas de 20: {}'.format(cedulas20))
if valor >= 10:
	cedulas10 = valor // 10
	valor -= cedulas10 * 10
	print('Cédulas de 10: {}'.format(cedulas10))
if valor >= 5:
	cedulas5 = valor // 5
	valor -= cedulas5 * 5
	print('Cédulas de 5: {}'.format(cedulas5))
if valor:
	cedulas1 = valor
	print('Cédulas de 1: {}'.format(cedulas1))

	
Calculadora de cédulas utilizado break: 
	
valor = int(input('Digite o valor em R$ '))

while True: 
	if valor >= 100:
		cedulas100 = valor // 100
		valor -= cedulas100 * 100
		print('Cédulas de 100: {}'.format(cedulas100))
		if not valor: 
			break
	if valor >= 50:
		cedulas50 = valor // 50
		valor -= cedulas50 * 50
		print('Cédulas de 50: {}'.format(cedulas50))
		if not valor: 
			break
	if valor >= 20:
		cedulas20 = valor // 20
		valor -= cedulas20 * 20
		print('Cédulas de 20: {}'.format(cedulas20))
		if not valor: 
			break
	if valor >= 10:
		cedulas10 = valor // 10
		valor -= cedulas10 * 10
		print('Cédulas de 10: {}'.format(cedulas10))
		if not valor: 
			break
	if valor >= 5:
		cedulas5 = valor // 5
		valor -= cedulas5 * 5
		print('Cédulas de 5: {}'.format(cedulas5))
		if not valor: 
			break
	if valor:
		cedulas1 = valor
		print('Cédulas de 1: {}'.format(cedulas1))
		break	
		
Calculadora de bilhetes cinema: 
	
	total = 0
dinheiro = 0

while True:
    idade = input('Qual a sua idade? ')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1

    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15

    dinheiro += ingresso

media = dinheiro / total
print('Total de pessoas {}'.format(total))
print('Total de dinheiro {}'.format(dinheiro))
print('Total de pessoas {}'.format(media))

	
	
	
