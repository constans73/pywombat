
numero = int(input("introduce numero\n"))
resultado = numero

while numero > 2:
	resultado = resultado * (numero - 1)
	numero -=1
print ("Su factorial es:", resultado)




#####################   solucion con una funcion y otro enunciado    #########################

"""
Definir una función la cual nos permita conocer el factorial de un número.

    La función debe tener por nombre factorial.
    La función debe poseer el parámetro valor.
    La función debe retornar el factorial del parámetro.
    La función no debe hacer uso de ningún tipo ciclo.



def factorial(valor):
   if valor == 1:
       return valor
   else:
       return valor * factorial(valor-1)

 """      