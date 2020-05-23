

sentencia = input ("Escribe una frase\n")
llave = input ("introduce el grado de codificacion\n")


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

print (frase_modificada)
