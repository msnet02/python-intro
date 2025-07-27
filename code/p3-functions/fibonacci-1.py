# Programa: fibonacci-1.py
# Creación: 26/07/2025

def fibonacci(lim_sup):
    result = [] # Se crea un lista vacía que contendrá los elementos de la sucesión
    a, b = 0, 1 # Simplificación gracias a la asignación doble
    
    # Bucle para añadir a la lista todos los elementos de la sucesión
    while a < lim_sup:
        result.append(a)
        a, b = b, a + b # Intercambio de valores gracias a la asignación doble
    
    return result # Devuelve la sucesión como una lista

# Main code
sucesion = fibonacci(1000) # El mayor elemento de la sucesión deberá ser menor que 1000
print(sucesion)
