#Area de un circulo
#La forma del area del circulo es la siguiente (A = π * (r**2) )
π = 3.1416 #Definimos el valor de π
print("Vamos a calcular el area de un circulo")
radio = input("Ingresa el valor del radio de tu circulo en cm, solo el valor, ya sea entero o decimal:")#pedimos al usuario que ingrese el valor del radio
area = π * (float(radio)**2)
print(f"El area del circulo es: {area} cm \n \n")


#Indice de masa corporal
#La formula para saber el indice de masa corporal es: IMC = peso / (altura**2)).
print("Vamos a calcular tu indice de masa corporal")
peso = input("Ingresa tu peso:")
altura = input("Ingresa tu altura:")
IMC = float(peso) / float(altura)**2
print(f"Tu indice de masa corporal es: {IMC}")