while True:
	try:
		number = int(input('Digite um número para ser fatorado: '))

		def fatorado(number):
			resul = 1
			for numeros in range(1, number + 1):
				resul *= numeros
			return resul

		print(f'O número {number} fatorado é: ',fatorado(number), '\n\nTeste outro número🤓👇')
	except ValueError:
		print('Por favor, digite um número inteiro')
		continue