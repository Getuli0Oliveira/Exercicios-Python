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

-------------------------------------------------------

# Funções

# Definição da função
def realce():
	print('|', '-'*10,'|')

# Programa principal
realce()
print('     Menu')
realce()

--
# Definição da função
def mensagem(msg):
	print('-' * 30)
	print(msg)
	print('-' * 30)

# Programa principal
mensagem('SISTEMA DE ALUNOS')
mensagem('...')
mensagem('...')

--
# Definição da função
def soma(a, b):
	s = a + b 
	print(s)

# Programa principal
soma(4,5)
soma(8,9)
soma(2,1)

--
# Definição da função
def soma(a, b):
	print('A = {} e B = {}'.format(a, b))
	s = a + b 
	print('A soma de A + B = {}'.format(s))

# Programa principal
soma(4,5)
soma(8,9)
soma(2,1)
	
--
# Esta função retorna uma Tupla

# Definição da função
def contador(*num):
	tam = len(num)
	print('Recebi os valores {} e são ao todo {}'.format(num, tam))

# Programa principal	
contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)

# Paramêtros são dados recebidos pela função 

def sub2(a,b):
	res = a - b
	print(res)

	
sub2(b=7,a=5)

# Parâmetros opcionais: 

def soma3(x = 0,y = 0,z = 0): --> Cabeçalho da função
	res = x + y + z
	print(res)
	
soma3(1,2,3)
soma3(1,2) 	#z foi omitido
soma3(1,) 	#y e z foram omitidos
soma3()			#x, y e z foram omitidos

# Função adaptável: 

def borda(s1):
	tam=len(s1)
	if tam: 
		print('+','-' * tam,'+')
		print('|',s1,'|')
		print('+','-' * tam,'+')


borda('Olá, mundo')
borda('Lógica de programação e Algorítmos')

-------------------------------------------------------------
# Escopo de variáveis: 

Um escopo é o que determina onde vai ser usada a variável

* Escopo local:

* Criado sempre que uma função é chamada 
* Variáveis criadas, seja no campo de um parâmetro ou no corpo da função.
* Essas variáveis só existem dentro daquela própria função.
* Não pode ser acessada por outras funções. 

* Escopo global:
	
* Criado no programa principal.
* Variáveis globais pertencem a um escopo global e são criadas dentro de um programa principal.
* Uma variável global existe também em todas as funções invocadas ao longo do programa.

def comida():
	print(ovos)

ovos = 12  # Variável global
comida()	 # Variável local

--

def comida():
	ovos = 12  --> Variável local
	bacon()
	print(ovos)

def bacon():
	ovos = 6 	 --> Variável local

comida()
	
# A instrução global: 

def comida():
	global ovos
	ovos = 'Comida'

ovos = 'global'
comida()
print(ovos)

--------------------------------------------------------------------

# Retorno de valores em funções: 

* Procedimento (procedure) - Uma rotina sem retorno
* Função - uma rotina que retorna um valor ou dados a quem a invocou

def soma3(x=0,y=0,z=0):
	res = x + y + z
	return res

retornando = soma3(1,2,3)
print(retornando)

# forma alternativa simplificada
print(soma3(2,2))

--

# Validação de string:

def valida_string(pergunta, min, max):
	s1 = input(pergunta)
	tam = len(s1)
	while ((tam < min) or (tam > max)):
		s1 = input(pergunta)
		tam = len(s1)
	return s1

x = valida_string('Digite uma string: ', 10, 30)
print('Você digitou a string {}.\n Dado válido. Encerrando o programa...'.format(x))

# Recursos avançados com funções: 

* Exceção
A sintaxe está correta, mas o erro está na execução do programa. 

while True: 
	try:
		x = int(input('Por favor digite um número: '))
		break
	except ValueError: 
		print('Oops! Número inválido. Tente novamente...')
		
--

def div():
	try: 
		num1 = int(input('Digite um número: '))
		num2 = int(input('Digite um número: '))
		res = num1 / num2
	except ZeroDivisionError:
		print('Oops! Erro de divisão por zero')
	except:
		print('Algo de errado aconteceu...')
	else:
		return res
	finally:
		print('Executará sempre!')

print(div())

# Função como parâmetro de função.

def imprime_com_condicao(num, fcond):
	if fcond(num):
		print(num)

def par(x):
	return x % 2 == 0
def impar(x):
	return not par(x)


imprime_com_condicao(5, par)

# Função lambda

res = lambda x: x * x 
print(res(3))

soma = lambda x, y: x + y
print(soma(3, 5))

# Aula prática 5 e manipulação de arquivos

* Arquivos
	Abrir arquivo: open()
	Fechar arquivo: arquivo.close()
* Ler arquivo: 
	arquivo.read()
	arquivo.readlines()
* Escrever no arquivo: 
	arquivo.write()	
-------------------------------------------------------
# MODO |                   OPERAÇÕES 		            	-
#  r   | Leitura                                      -
#  w   | Escrita, apaga o conteudo se existir         -
#  a   | Escrita, mas preserva o conteúdo se existir  -
#  b   | Modo binário                                 -
#  +   | Atualização (leitura e escrita)              -
-------------------------------------------------------

Interactive help ---> help() e para sair quit 
Serve para ajudar no código, explicando uma função e/ou features que ela possui.

def soma(x=0,y=0,z=0):
	return x,y,z
"""
:param x: valor inteiro opcional
:param y: valor inteiro opcional
"""
print(soma(3,2))
help(soma)

# Exercício 1 - 

def valida_int(pergunta, min, max):
	x = int(input(pergunta))
	while ((x < min) or (x > max)):
		x = int(input(pergunta))
	return x
	

def fatorial(num):
	fat = 1 
	if num == 0:
		return fat 
	for i in range(1,num+1, 1):
		fat *= i 
	return fat

x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('{}! = {}'.format(x,fatorial(x)))


# Exercício 2 - 

def valida_int(pergunta, min_value, max_value):
    x = int(input(pergunta))
    while ((x < min_value) or (x > max_value)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')  # Escreve texto e cria caso não exista
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try: 
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else: 
        a.write('{};{}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        print(a.read())
    finally:
        a.close()


arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criaArquivo(arquivo)

while True:
    print('Menu')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionado...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar selecionada...')
        listarArquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa')
        break


# Tuplas, listas, dicionários e strings: 

Variáveis simples: Armazena um item somente.
Variáveis compostas: Armazena múltiplus dados. 

Variável[0], Variável[1], Variável[2], Variável[3]

Estrutura de dados é um conjunto de dados organizados de maneira específica na memória.

# Tupla

* Estrutura de dados
* A tupla é imutável
* Representada em Python por parênteses

mochila = ('Machado','Camisa', 'Bacon', 'Abacate')
print(mochila[0:2]) # Output - ('Machado', 'Camisa')

mochila[2] = 'Ovos' = TypeError - Não podemos alterar.

for item in mochila: 
	print('Na minha mochila tem {}'.format(item))

Com range: 
	
tam = len(mochila)
for i in range (0, tam, 1):
	print('Na minha mochila tem {}'.format(mochila[i]))
	
Não podemos alterar a estrutura, mas podemos somar, por meio da manipulação de variáveis. 

mochila = ('Machado','Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo','Canivete')
mochila_grande = mochila + upgrade

print(mochila_grande)

# Desempacotamento de parâmetros em funções

* O simbolo '*' simboliza desempacotamento.

def soma(*num):
	soma = 0 
	print('Tupla: {}'.format(num))
	for i in num:
		soma += i
	return soma

print('Resultado: {}\n'.format(soma(1,2)))
print('Resultado: {}\n'.format(soma(1,2,3,4,5,6,7,8,9)))

# Listas

* Estrutura de dados dinâmica
* Podemos alterar dados e tamanho 
* Indexadas por valores numéricos inteiros
* Representadas em Python por colchetes []

mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
print('Lista:', mochila)

* Podemos alterar:
	
mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
print('Lista:', mochila)

mochila[2] = 'Laranja'
print('Lista:', mochila)

*Manipulando listas: 

mochila.append('Ovos') # Acrescenta um item ao final da lista
print('Lista', mochila)

mochila.insert(1,'Canivete') # Acrescenta um item em uma posição específica da lista
print('Lista', mochila)	

del mochila[1] # Remove um item de acordo com a posição no índice
print('Lista:', mochila)

mochila.remove('Ovos') # Remove um item da lista pelo nome
print('Lista: ', mochila)

* Cópia de listas: 

x = [5,7,9,11] #Copia variável 
y = x

print(x)
print(y)

--

x = [5,7,9,11]  #Se alterarmos a cópia(y), alteramos a original(x)
y = x

print(x)
print(y)

y[0] = 10
print(x)
print(y)

* Desta forma criamos uma cópia na memoria, podendo alterar a cópia -->

x = [5,7,9,11]
y = x[:]

print(x)
print(y)

y[0] = 50
print(y)

* A lista é considera um objeto, portanto POO

*Método é equivalente à função:
	
mochila.append('Ovos')
variável.função(parâmetro)

# Strings e listas dentro de listas: 

*Dupla indexação

mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
mochila[0][0] # Acessa primeiro o item do indice e depois o length da string. Portanto = mochila[0][0] == M

Com range 

mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
for item in mochila: 
	for letra in item:
		print(letra, end='')
	print()

Sem range

mochila = ['Machado','Camisa', 'Bacon', 'Abacate']
for i in range(0,len,(mochila),1): 
	for j in range(0,len,(mochila[i],1)):
		print(mochila[i][j], end='')
	print()

* Listas dentro de listas: 
	
mochila = [['Cebola', 0,39],['Tomate, 0.49],['Maça', 0,89]]
--
			     


item = []
mercado = []			     

for i in range(3):
	item.append(input('Digite o nome do item: '))
	item.append(int(input('Digite a quantidade:')))
	item.append(float(input('Digite o valor: ')))
	mercado.append(item[:])
	item.clear() # Limpa a seleção anterior depois de estar armazenada, evitando que o item apareça novamente. 
print(mercado)     
			    
Output --> [['Cebola', 10, 0.69], ['Tomate', 5, 0.79], ['Abacate', 5, 1.25]]
			     
* Forma simplificada: 
			     
 mercado = []			     

for i in range(3):
	nome = (input('Digite o nome do item: '))
	qtd = (int(input('Digite a quantidade:')))
	valor = (float(input('Digite o valor: ')))
	mercado.append([nome, qtd, valor])
print(mercado)

--
			     
mercado = []			     

for i in range(3):
	nome = (input('Digite o nome do item: '))
	qtd = (int(input('Digite a quantidade:')))
	valor = (float(input('Digite o valor: ')))
	mercado.append([nome, qtd, valor])
print(mercado)

soma = 0

print('Lista de compras')
print('-' * 20)
print('Item | Quantidade | Valor unitário | Total do item')

for item in mercado:
	print('{} |{}| {} |{}'.format(item[0], item[1], item[2], item[1] * item[2]))
	soma += item[1] * item[2]
print('-' * 20)
print('Total a ser pago {}'.format(soma))
			     
# Dicionários: 
			     
* Estrutura de dados dinâmica
* Podemos alterar dados e tamanho 
* Indexados por chaves
* Representadas em Python por chaves {}
	
							 
# O item antes do : é o index e após o : é o dado							 

game = {'nome': 'Super Mario',
			 'desenvolvedora': 'Nintendo',
			 'ano':1990}

print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])
							 
*	values: obtém somente os dados 						 
*	keys: obtém somente as chaves					 
*	items: obtém o par chave:dado		
							 
print(game.values()) --> Imprime somente os valores do dicionário.
	Output - dict_values(['Super Mario', 'Nintendo', 1990])
							 
for i in game.values():							 
	print(i)						 
	Output - Super Mario
			 Nintendo
			 1990		
							 
print(game.keys()) --> 	Imprime somente as chaves do dicionário.						 
	Output - dict_keys(['nome', 'desenvolvedora', 'ano'])						 
							 
for i in game.keys():							 
	print(i)							 
	Output - nome
			 desenvolvedora
			 ano

print(game.items()) --> 	Imprime o par chave:dado.						 
	Output - dict_items([('nome', 'Super Mario'), ('desenvolvedora', 'Nintendo'), ('ano', 1990)])					 
							 
for i,j in game.items():
	print('{} = {}'.format(i,j))						 
	Output - nome = Super Mario
			 desenvolvedora = Nintendo
			 ano = 1990					 
							 
# Dicionário dentro de lista
							 
games = []

game1 = {'nome': 'Super Mario',
			 'desenvolvedora': 'Nintendo',
			 'ano':1990}
game2 = {'nome': 'Zelda Ocarina of Time',
			 'desenvolvedora': 'Nintendo 64',
			 'ano':1998}
game3 = {'nome': 'Pokemon Yellow',
			 'desenvolvedora': 'Nintendo Game Boy',
			 'ano':1999}


games = [game1, game2, game3]	
print(games)
							 
--	
* Adicionando os dados pelo teclado e for aninhados 1º for anda na lista 2º for anda no dicionário. 							 
							 
game = {}
games = []

for i in range(3):
	game['nome'] = input('Qual o nome do jogo?')
	game['videogame'] = input('Para qual video-game ele foi lançado?')
	game['ano'] = input('Qual o ano de lançamento?')
	games.append(game.copy())
print('-' * 20)
for e in games:
	for i, j in e.items():
		print('O campo {} tem valor {}.'.format(i,j))	
							 
# Dicionário com listas dentro:
							 
games = {'nome':['Super Mario','Zelda Ocarina of Time','Pokemon Yellow'],
			'videogame': ['Super Nintendo', 'Nintendo 64', 'Nintendo Game Boy'],
			'ano': [1990,1998,1999]}
print(games)							 

--							 
* Adicionando os dados com entradas no teclado e estrutura de repetição em for. 
							 
games = {'nome':[],'videogame':[], 'ano':[]}
for i in range(3):
	nome = input('Qual o nome do jogo? ')
	videogame = input('Qual o nome do video-game?')
	ano = input('Qual o ano de lançamento?')
	games['nome'].append(nome)
	games['videogame'].append(videogame)
	games['ano'].append(ano)
print('-' * 20)
print(games)	
							 
# Trabalhando com métodos em strings:
							 
* Uma string é imutável
* Só pode ser alterada se estiver numa lista
							 
s1 = 'Algorítmos'
print(s1)
s1[0] = 'a'		# Dá erro pois não permite alterações.
							 

s1 = list('Algorítmos') # Se transformarmos a string em lista conseguimos alterar
print(s1)
print(''.join(s1))
s1[0] = 'a'
print(''.join(s1))							 
							 

s1 = 'Lógica de Programação e Algoritmos'
s1.startswith('Lógica')

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('Algoritmos')

s1 = 'Lógica de Programação e Algoritmos'
s1.endswith('algoritmos')

s1 = 'Lógica de Programação e Algoritmos'
s1.lower().endswith('algoritmos')

s1 = 'Lógica de Programação e Algoritmos'
print(s1.upper())
print(s1.lower())		
							 
s1 = 'Lógica de Programação e Algoritmos'
s1.count('a')

# Quebrando strings:
							 
s1 = 'Lógica de Programação e Algoritmos'
s1.split(' ')		
							 
# Substituindo strings:							 
							 
s1 = 'Lógica de Programação e Algoritmos'
s1.replace('Lógica', 'Lógico')		
							 
# Validando tipos de dados: 
							 
s1 = 'Lógica de programação e Algoritmos'
s2 = '42'

print(s1.isalnum) #False  
print(s2.isalnum) #True		
							 
s1 = 'Lógica de programação e Algoritmos'
s2 = '42'

print(s1.isalpha) #False  
print(s2.isalpha) #False							 

s1 = 'LógicadeprogramaçãoeAlgoritmos'
s2 = '42'

print(s1.isalpha) #True  
print(s2.isalpha) #False							 
