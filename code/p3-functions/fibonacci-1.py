# Programa: fibonacci-1.py
# Creación: 26/07/2025

def fibonacci(lim_sup):
    a, b = 0, 1 # Simplificación gracias a la asignación doble
    result = [a, b] # Se crea una lista con los dos primeros elementos de la suceción
    
    # Bucle para generar la sucesión, desde el tercer elemento en adelante
    while a < lim_sup:
        a, b = b, a + b # Intercambio de valores gracias a la asignación doble
        if b < lim_sup:
            result.append(b)

    return result # Devuelve la sucesión como una lista

# Main code
sucesion = fibonacci(1000) # El mayor elemento de la sucesión deberá menor que 1000
print(sucesion)
