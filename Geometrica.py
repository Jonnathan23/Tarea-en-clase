#Inicialización de variables
p = float(input("Ingrese la probabilidad de falla % ")) / 100
q = 1- p
x = int(input("Numero de la prueba en la que ocurre el exito "))

px = p*(1-p)**(x-1)

print(f'La probabilidad de fallo en el intento {x} es de: {px*100} %')
