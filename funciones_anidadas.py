def funcion_padre():
	valor = 10

	def funcion_anidada():
		nonlocal valor
		valor = 20
		print(f'Valor en función anidada es {valor}')

	print(f'Valor en función padre antes es {valor}')
	funcion_anidada()
	print(f'Valor en función padre después es {valor}')

funcion_padre()
