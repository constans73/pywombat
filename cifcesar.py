def cifrado(sentencia, llave=10):
	llave = int(llave)
	sentencia = sentencia.lower()
	letras = "abcdefghijklmnñopqrstuvwxyz"   #longitud 26

		
	numero = 0
	frase_modificada =""
	while numero != len(sentencia):	
	
		if sentencia[numero] in letras:
		
			salto = letras.index(sentencia[numero]) + llave				#se elige el salto que tiene que dar indice de
																	#letras mas el salto por el usuario
			if salto > 26:
				salto = salto - 27										#si el salto excede el limite de 26
				frase_modificada = frase_modificada + letras[salto]
			else:
				frase_modificada = frase_modificada + letras[salto]
		
		else:

			frase_modificada = frase_modificada + sentencia[numero]		#si nes caracter de letras se queda igual

		numero += 1

	return frase_modificada


texto = input ("Introduce el texto a codificar\n")
grado = input ("Introduce el grado de codificacion\n")


if grado:

	codigo_cifrado = cifrado (texto, grado)			#si quiero meter grado de cifrado
	print (codigo_cifrado)

else:
	codigo_cifrado = cifrado (texto)				#si quiero el grado por defecto
	print (codigo_cifrado)
