

sentencia = input ("Escribe una frase\n")
llave = input ("introduce el grado de codificacion\n")


llave = int(llave)
sentencia = sentencia.lower()
letras = "abcdefghijklmnñopqrstuvwxyz"   #longitud 26
	




for i in sentencia:
	
	salto = letras.index(i) + llave
	sentencia = sentencia.replace (i,letras[salto])
	



print (sentencia)


"""
if salto > 26:
			salto =  salto - 27

			sentencia = sentencia.replace (i,letras[salto])
		else:
			sentencia = sentencia.replace (i,letras[salto])

"""

#tercera modificacion