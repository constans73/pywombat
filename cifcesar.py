def cifrado(sentencia, llave=10):
	llave = int(llave)
	sentencia = sentencia.lower()
	letras = "abcdefghijklmnñopqrstuvwxyz"   #longitud 26
	
	for i in sentencia:

		if i in letras:

			salto = letras.index(i) + llave
				
			if salto > 26:
				salto =  salto - 27					#si rompe la longuitud de letras

				sentencia = sentencia.replace (i,letras[salto])
			else:
				sentencia = sentencia.replace (i,letras[salto])


	return sentencia



texto = input ("Introduce el texto a codificar\n")
grado = input ("Introduce el grado de codificacion\n")


if grado:

	codigo_cifrado = cifrado (texto, grado)			#si quiero meter grado de cifrado
	print (codigo_cifrado)

else:
	codigo_cifrado = cifrado (texto)				#si quiero el grado por defecto
	print (codigo_cifrado)
