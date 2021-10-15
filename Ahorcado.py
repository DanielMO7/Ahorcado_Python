import random
from os import system

IMAGES = ['''

	+---+
	|	|
		|
		|
		|
		|
		|
		============''',
	'''

	 +---+
	 |	 |
	 O	 |
		 |
		 |
		 |
		 |
		 ============''', 
	'''

	 +---+
	 |	 |
	 O	 |
	 |	 |
		 |
		 |
		 |
		 ============''',
	'''

	 +---+
	 |	 |
	 O	 |
	/|	 |
		 |
		 |
		 |
		 ============''',
	'''
         
     +---+
	 |	 |
	 O	 |
	/|\	 |
		 |
		 |
		 |
		 ============''',
	'''

	 +---+
	 |	 |
	 O	 |
	/|\	 |
	 |	 |
		 |
		 |
		 ============''',
	'''

	 +---+
	 |	 |
	 O	 |
	/|\	 |
	 |	 |
	/	 |
		 |
		 ============''',
	'''	 

	 +---+
	 |	 |
	 O	 |
	/|\	 |
	 |	 |
	/ \	 |
		 |
		 ============
'''
]

WORDS = [
	'diego',
	'laura',
	'juan',
	'dayana',
	'juan',
	'karen',
]

def random_word():
	idx = random.randint(0, len(WORDS)-1)
	return WORDS[idx]

def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print('')
	print(hidden_word)	

def determinar_fin(hidden_word): # Añado esta funcion para definir si se encuentra algun gion en el hidden_word
	return '-' not in hidden_word

def bienvenida():
    print('*' * 50)
    print('* TE DOY LA BIENVENIDA AL JUEGO DEL AHORACADO *')
    print('*' * 50)
    print('* Recuerda que tienes 7 vidas, Mucha suerte. *')

def vida(tries):
	vidas = 7
	vid_total = 0
	if tries != 0:
		vid_total = vidas - tries
		print('*' * 15)
		print ('   Vidas: ', vid_total)
		print('*' * 15)

def pedir_letra(hidden_word, letras_erroneas):
	valida = False
	while not valida:
		current_letter = input('Digite una letra (a-z): ').lower()
		valida = 'a' <= current_letter <= 'z' and len(current_letter) == 1
		if not valida:
			print(' Error, has ingrezado un número a algún otro caracter.')
		else:
			valida = current_letter not in hidden_word + letras_erroneas
			if not valida:
				print(' Letra repetida, prueba con otra.')
	return current_letter
    
def procesar_letra(cont):
	if cont > 0:
		print('----------------------------------------')
		print('¡Genial! Has acertado ', cont ,'letra.')
		print('----------------------------------------')

def jugar_otra_vez():
	return input('¿Deseas jugar otra vez? s = Sí,  n = No:  ')
	
def despedida():
    print('*' * 68)
    print('* Gracias por jugar al ahorcado. ¡Hasta pronto! *')
    print('*' * 68)		

def run():
	word = random_word().lower() # Utilizo la funcion lower para convertir a minuscula todas las letras en mayuscula
	hidden_word = ['-'] * len(word)
	tries = 0
	letras_erroneas = []
	

	while True:
		cont = 0
		vida(tries)
		display_board(hidden_word, tries)
		current_letter = pedir_letra(hidden_word,  letras_erroneas)

		letter_indexes = []
		for idx in range(len(word)):
			if (word[idx] == current_letter):
				cont += 1 
				letter_indexes.append(idx)
		vida(tries)
		procesar_letra(cont)				
				
				
		if (len(letter_indexes) == 0):
			tries += 1
			print('----------------------------------------')
			print('Tu letra no se encuentra en la palabra')
			print('----------------------------------------')
			letras_erroneas.append(letter_indexes)


			if (tries == 7):
				display_board(hidden_word, tries)
				print('')
				print('-------------------------------------------------')
				print("¡Perdiste! La palabra correcta es {}".format(word))
				print('-------------------------------------------------')
				print('')
				break

		else:
			for idx in letter_indexes:
				hidden_word[idx] = current_letter
			letter_indexes = []	

		if determinar_fin(hidden_word): # Al invocar esta funcion si resulta ser correcta entonces nos sale el siguiente mensaje
			print('')
			print('------------------------------------------------')
			print("¡Ganaste! La palabra correcta es {}".format(word))
			print('------------------------------------------------')
			print('')
			break	
			
		try:
			hidden_word.index('_')
			

		except ValueError:
				print('')
				

if __name__ == '__main__':
	
	while True:
		system("cls")
		bienvenida()
		run()
		if jugar_otra_vez() != 's': break
	despedida()	

