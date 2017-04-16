print("Seria um cliché, usar Hello World!") 

# comentários necessitam de um cardinal
# o print serve para imprimir o resultado do código que estamos usar

print(1 + 2)
print(5 - 3)

# também podemos criar variáveis por assignment,  usando "="

x = 1 + 2
print(x)



# esta variável fica guardada podendo ser-lhe aplicadas outras operações

print(x * x)	# multiplicações
print(x / 2)	# divisão

print(x > 9)	# lógica, x é maior que 9?
print(x == x)	# lógica, x é o mesmo que x?
print(x == 4)	# lógica, x é o mesmo que 4?

# outras operações 

print(x ** 2)	# exponenciais
print(18 / x)
print(18 % x)	# o módulo, calcula o Resto numa divisão
print(x ** 1/2) # raiz quadrada

# alternativa
import math

math.sqrt(x) 	# as bibliotecas trazem funções extra.

### Exercício 1
# Usando a variável x
# Com uma taxa de juros de 5%, quanto valeriam 4000â‚¬ depositados, após 3 anos?

# Resoluções possíveis:
# print(4000 * 1.05 ** x)
# print(x * 1000 * 1.05 ** 3)
# print(x * 1000 * 1.05 * x) 


#--------------Variáveis--------------

# Os nomes de variáveis devem ser práticos, fáceis de memorizar e de escrever.
# Não devem conter acentos nem devem começar com letra maiúscula

melhor_workshop_do_mundo = "data_science.py"	# faz sentido, mas pouco prático
print(melhor_workshop_do_mundo) 				

jest = "data_science.py"
print(jest)                                     # duas variáveis podem ter o mesmo valor

# Às variáveis são atribuídos valores que podem ser de vários tipos. Os mais comuns são:
a = 4.5
print(type(a))			# Float - Pode conter uma parte décimal
print(type(x))			# Int - Contém apenas um inteiro 
print(type(jest))		# String (str) - Contém uma ou várias palavras
validade = x > 9		# Pegando no exemplo lógico usado anterior a variável vai se verdadeira ou falsa 
print(type(validade))	# Boolean (bool)

# Q: Em operações entre uma variável do tipo int e uma variavel do tipo float espera-se
# que o resultado seja de que tipo?
# R: Float (CHOCANTE)

### Exercício 2
# Usando só variáveis
# Com uma taxa de juros de 5%, quanto valeriam 4000€ depositados, após 3 anos?

# Resoluções possíveis:
# o x já foi definido com sendo = 3
juros = 1.05
valor = 4000
resultado = valor * juros ** x 
print (resultado)

# Vantagem do uso de varíaveis: Se quisessemos obter o resultado para os mesmos
# dados, mas, por exemplo, para uma taxa de juros bastava alterar a variável juros.

# Se tentarmos imprimir a frase "O resultado é:" e o resultado:
# print("O resultado é: " + resultado)	# Dá erro! --> "must be str, not float"

# Ou seja, temos de converter a variável resultado (float) numa variável (string):

resultado = str(resultado)
print ("O resultado é: " + resultado)

#--------------Listas--------------

# Listas são a melhor maneira de guardar diversos valores sem ter de recorrer a muitas variáveis.

# Por exemplo, se quisermos guardar a idade das pessoas que estão na sala faríamos
# idade1 = 17
# idade2 = 20
# idade3 = 30
# ...
# OU
# Criamos uma lista
# idade = [17, 20, 30,...]
# Uma lista pode conter variáveis de vários tipos inclusive listas!
# Por exemplo, podemos guardar os nomes e as idades correspondentes:
participantes = ["Rute", 20, "Hugo", 19, "Calil", 28, "Coelho", 24]
print(participantes)
# OU, ainda mais organizado:
# 	participantes = [["Rute",20],
# 					["Hugo",17],
#					["Calil",28],
#					["Coelho",25]]

# Como imprimir/selecionar um ou vários elementos de uma lista?

# Por exemplo, queremos saber qual o terceiro elemento da lista "participantes" :

# ATENÇÃO: Em Python, a contagem dos elementos de uma lista começa em 0,
# ou seja, o primeiro elemento fica no lugar 0!

print(participantes[2]) # código: nomedalista[elemento]

# Imprime "Hugo"
# Ou, começando no final da lista, o último elemento corresponde ao lugar [-1] e 
### Exercício 3
# Como recuperamos o elemento "Hugo" a utilizar contagem decrescente
# Exemplo
print(participantes[-1]) # devolve "24"

# Solução é print(participantes[-6])

# Para a segunta lista fariamos participantes[[2][1]]
# print(participantes[1][0])

# Imaginemos agora que queremos criar uma segunda lista, igual à primeira, mas sem o Coelho e a sua idade:

participantes2 = participantes		# Criamos um intervalo que vai desde o primeiro 
print(participantes2)				# elemento até ao 6º, sem o incluir.
# Ou participantes2 = participantes[:6] 

# Ou, em vez de criar uma lista nova podemos apenas eliminar os elementos "Coelho" e "25":
del(participantes[6])
del(participantes[6]) # Não esquecer que eliminamos o 6º elemento na linha anterior, logo "25" passou a ser o 6º elemento
print(participantes)

# Para adicionar novamente fazemos:
participantes = participantes + ["Coelho", 25] # ou participantes.append("Coelho") e participantes.append(25)                  
print(participantes)



# Vamos agora alterar a idade da Rute para 21:
participantes2[1] = 21 
print(participantes2)


### Exercicio 4 - Qual a média das idades dos participantes?
# Resolução:
# media = (participantes[1]+participantes[3]+participantes[5]+participantes[7])/4
# print(media)

# Nota Importante: quando criamos, por exemplo, uma lista x e uma lista y e definimos y por sendo igual a x
# Se alterarmos algum elemento da lista y este elemento também é alterado na lista x, isto porque ambas as variáveis
# estão a apontar para a mesma lista (não gosto desta explicação).
# Para contornar isto fariamos: y = x[:], y corresponderia então a uma cópia da lista definida em x e não à própria lista! 
# Podendo alterar-se y sem afetar x.


# --------------- Functions --------------------

# Bocado de código que pode serve para ser aplicado numa dada tarefa. Por exemplo, 
# no tema "Variáveis" introduzimos a função type() que é usada para retornar o tipo 
# da variável que escolhemos.
# Outras funçoes uteis:
# max() --> serve para determinar o maior elemento de uma lista, por exemplo.
# round() --> serve para aredondar valores
# len() --> serve para ver o tamanho de uma lista
# help() --> serve para obter informação à cerca de outras funções do Python
# Existem outras funções muito uteis e que podem tornar a execuçao do nosso código muito mais simples,
# a melhor maneira de as descobrir é pesquisar na net o que queremos fazer e grande parte das vezes 
# encontraremos respostas que nos encaminham para funções existentes no Pyhton.

# Uma das funções que mais usaremos, para além do print() que como já vimos serve para......
# é a função input() que serve para guardar numa variável uma String introduzida pelo utilizador
# Por exemplo,

idade = input("Qual a idade que davam ao Coelho? ") 
print(type(idade)) # todo o tipo de dados introduzidos pelo comando input serão do tipo string

# Imaginemos agora que queremos com essa idade calcular a sua data de nascimento

# print("O ano de nascimento dele é então " 2017-idade)  # daria erro pois nao podemos somar um int com uma str
# para podermos somar temos que converter a idade (tipo String) num integer usando o comando int()

idade = int(idade) # ou entao logo no input idade = int(input("Qual a idade que davam ao Coelho? "))
print("O ano de nascimento dele é então ", 2017 - idade)

# --- Métodos
#
# Em Python tudo é um objeto e os objetos têm métodos a eles associados que variam consoante o seu tipo.
# Por exemplo, as variáveis que temos usado até agora são objetos e são de diferentes tipos: string, integer....
# Métodos são, então, funções especificas de cada objeto que variam consoante o tipo deste. Podendo não ser aplicaveis
# para tipos diferentes ou simplesmente comportarem-se de maneira diferente.
# 
# Por exemplo,
# Voltando à nossa lista de clubes, se quisermos adicionar o clube "Tondela" podemos faze-lo da forma que aprendemos
# quando falamos nas listas, isto é:
# clubes = clubes + ["Tondela"]
# 
# Ou podemos usar um método associado a objetos do tipo lista:
print(clubes.index("Braga"))
# Output 4

# O método index pode ainda ser aplicado a objetos do tipo string:
# Por exemplo, melhor_clube é do tipo string e está definido com "Sporting" 
print(melhor_clube.index("S"))
# Output 0

# Existem outro comandos que podem explorar em relação as listas como o comando pop que retira da posicao indicada o elemento e retorna o para fora
Braga = clubes.pop(4) # guardei-o na variavel nome
print(Braga)
print(clubes)

### Exercicio 5 - Como guardar os numeros inseridos por um utilizador numa lista?
# Resolução
numeros = list()
primeiro = int(input("Primeiro numero:"))
segundo = int(input("Segundo numero:"))
terceiro = int(input("Terceiro numero:")) # Como são 3 numeros não é muito cansativo mas imagina que eram 70?? Para fazer isso aprenderemos mais a frente os loops
numeros.append(primeiro)
numeros.append(segundo)
numeros.append(terceiro)
print(numeros)

# -------------- Tuplos -----------

# Os tuplos são tipo listas que podem conter elementos de qualquer tipo (int, str, listas, outro tuplos) 
# A grande diferença entre estes e as listas é que nao se pode alterar um elemento de um tuplo. 
# Tuplos sao IMUTAVEIS
# Vejamos o seguinte exemplo
clubes = ['Sporting','Academica','Porto','Benfica','Braga']
clubes[1] = 'Guimarães' 
print(a) #verificamos que foi mudado o 1 elemento (Academica) da lista

#Imaginemos que era um tuplo. Enquanto que as listas sao caracterizadas pelos parenteses rectos [] os tuplos sao caracterizados pelos parenteses curvos ()
clubes_1 = ('Sporting','Academica','Porto','Benfica','Braga')
#Se tentarmos a operação anterior vai dar erro clubes_1[1] = 'Guimarães', que é muito util para quando nao queremos que os dados sejam alterados
#Temos outras operações para realizar com tuplos como

print(len(clubes_1)) # diz nos o tamanho do tuplo
print(clubes_1.index('Porto'))# diz nos a posição da primeira vez que aparece Porto
print('Sporting' in clubes_1) # Atraves de um booleano (TRUE or FALSE) diz nos se o Sporting esta dentro do tuplo


#Nao é por nao os podermos alterar que nao os podemos consultar
melhor_clube = clubes_1[0]
print("o melhor clube é", melhor_clube)



# --------------- Dicionarios --------------------

#Agora vamos ver o que são dicionarios:
idades = {'Rute':20, 'Hugo':19, 'Coelho':24, 'Calil':28}

# Os dicionarios sao caracterizados pelo caracter {}. Cada elemento do dicionario, separados por virgulas, tem 2 componentes. 'Rute':19 é um elemento onde 'Rute' é a chave e 19 é o valor.
#Enquanto que nas listas e nos tuplos para aceder aos elementos acedia-se pela sua posição, nos dicionarios só se pode consultar pela chave porque os dicionarios não têm ordem!!
print(idades)
print(idades)
print(idades)
print(idades) # Como podem ver as ordens que apareceram nos prints nao foram iguais

# Entao se quisessemos a idade da Rute estaria errado fazer idades[0]. Para a conseguir faziamos 
print(idades['Rute']) # que nos devolve 20

# Outras operacões que podemos realizar com os dicionarios são:
print(len(idades)) # diz quantos items tem o dict
del idades['Calil'] 
print(idades) # podemos eliminar o elemento associado a uma chave

# Se quiseremos adicionar o elemento de volta fazemos
idades['Calil'] = 28
print(idades)

# Existem ainda alguns metodos dos dicionarios
## metodos que nao modificam os dicionarios
#idades.copy() Devolve uma cópia do dict
#idades.items() Devolve um iterável de pares (chave,valor) de dict
#idades.keys() Devolve um iterável chaves de dict
#idades.values() Devolve um iterável de valores de dict
#idades.get(key,default=None)) Devolve o valor caso exista senão devolve default
## metodos que modificam os dicionarios
#idades.clear() Retira todos os elementos de dict
#idades.pop(key,default=None) Retira e devolve o elemento de key
#idades.popitem() Retira aleatoriamente e devolve um par
#idades.update(dict2) Adiciona os pares (chave,valor) de dict2 a dict
#idades.setdefault(key,default=None)) Como get mas actualiza o par com key:default




# --------------- Conditions --------------------
#
# Nos nosso programas iremos recorrer muito a condições do género: 
# if (condiçõe):		
#				códico

# Isto é, se a condição introduzida ( ) é verdadeira, então o programa executa o código introduzido.
# Por exemplo,
idade = int(input ("Qual é a sua idade? ")) # Usamos a função input para pedir a ao utilizador para introduzir um frase

if (idade<=12):
	print("É uma criança.")
elif (12<idade<18):
	print("É um jovem adulto.")
else:
	print ("É um adult.")

# Temos a primeira condição if(), a segunda condição elif() e para o caso de nenhuma das anteriores se verificar else.

# Exercicio Peça um número ao utilizador e devolva "É par." caso seja par ou "É ímpar" caso seja ímpar.

# Resolução

# numero = int(input("Introduza um número: "))
#if (numero%2 == 0): 
#	print ("É par.")
#else :
#	print("É ímpar.")


# --------------- Loops --------------------

# For and While Loop

# Vamos agora introduzir os cilos For e While, de uma forma geral ambos podem ser aplicados para resolver o mesmo problema
# desde que saibam como os aplicar.

# Queremos imprimir os nomes que estão numa lista separados:

nomes = ["Joana", "Tiago", "João", "Joana", "Marta", "Mariana", "Joana"]

# Usando o ciclo for 
for x in nomes: # A cada ciclo o x vai corresponder a um elemento da lista
	print(x)

print (x) # este print() está fora do loop logo vai corresponder apenas ao último elemento
# Alternativa
for i in range(len(nomes)):
	print(nomes[i])

# Usando o ciclo while
i = 0
while (i<len(nomes)): # enquanto a condição for verdadeira executa o código abaixo
	
	print (nomes[i])
	i +=1 # acrescenta uma unicade a i
#ou i = i+1

print (nomes[i])

# Exercicio Contar quantas vezes aparece o nome "Joana"

# Resolução 1 - For
#contador = 0
#for x in nomes: # A cada ciclo o x vai corresponder a um elemento da lista
#	if (x == "Joana"):
#		contador += 1
#print ("O nome Joana aparece", contador, "vezes")

# Resolução 2 - While
#contador = 0
#i=0
#while(i<len(nomes)): # A cada ciclo o x vai corresponder a um elemento da lista
#	i+=1
#	if ( nomes[i] == "Joana"):
#		contador += 1
#print ("O nome Joana aparece", contador, "vezes")


# --------------- Packages --------------------

# Use Terminal

python3 get-pip.py
pip3 install numpy

# Back to Python

import numpy

array([1, 2, 3, 4]) # does not work, why?

# you need to call it specifying the package

numpy.array([1, 2, 3, 4])

# since this can be tiresome, you might shorten the name

import numpy as np

# and then

np.array([1, 2, 3, 4])


### Final exercise
# Calculate area of circle from its circumference

C = 16.96

# We know C = 2*pi*r an that A = pi*r^2, so...

### SOLUTION (REMOVER NA VERSÃO PARA O WORKSHOP)
from math import pi 	# selective import
r = C / (2 * math.pi)	# gives us the radius

A = math.pi * r ** 2
print(A)				# result

###

### Final notes

# Let's take this opportunity to install every package you'll need in the following days
# Module 1
# pip3 install numpy # we already done this before, right? :-)
pip3 install pandas

# Module 2
pip3 install matplotlib

# Module 3
pip3 install sklearn
pip3 install seaborn
