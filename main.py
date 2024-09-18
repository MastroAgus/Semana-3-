#ejercicio 1 
import Repaso1

print ("----------------------------------------------------------------------------------------")
print ("Ejercicio 1")

circulo = Repaso1.area_A (float(input("define el radio del circulo: ")))
print (f"el area del ciculo es: {circulo}")

cuadrado = Repaso1.area_b (float(input("define la base del cuadrado: ")))
print (f"el area del cuadrado es: {cuadrado}")

base = (float(input("define la base del triangulo: ")))
altura = (float(input("define la altura del triangulo: ")))
triangulo = Repaso1.area_c (base, altura)
print (f"el area del triangulo es: {triangulo}")
print ("----------------------------------------------------------------------------------------")


#ejercicio 2 

import Repaso2

print ("----------------------------------------------------------------------------------------")
print ("Ejercicio 2")

circulo = Repaso2.perimetro_A (float(input("define el radio del circulo: ")))
print (f"el perimetro del ciculo es: {circulo}")

cuadrado = Repaso2.perimetro_b (float(input("define la base del cuadrado: ")))
print (f"el perimetro del cuadrado es: {cuadrado}")

base = (float(input("define la base del triangulo: ")))
altura = (float(input("define la altura del triangulo: ")))
triangulo = Repaso2.perimetro_c (base, altura)
print (f"el perimetro del triangulo es: {triangulo}") 

print ("----------------------------------------------------------------------------------------")



#ejercicio de Recursividad 1
import Recursividad

print ("----------------------------------------------------------------------------------------")
print ("Ejercicio Recursividad 1")

base = float (input ("base: "))
exponente = float (input ("exponente: "))

total = Recursividad.potencia (base, exponente)
print (f"la potencia da: {total}")

print ("----------------------------------------------------------------------------------------")


#ejercicio de Recursividad 2
import Recursividad2

print ("----------------------------------------------------------------------------------------")
print ("Ejercicio Recursividad 2")


n = int (input ("cuantos discos hay ? "))
Recursividad2.torres_de_hanoi(n, 'A', 'C', 'B')

print ("----------------------------------------------------------------------------------------")

