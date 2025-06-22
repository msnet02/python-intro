# Ambito Local versus Ambito Global

# Definición de la función local()
def local():
    # El ámbito de m es local
    m = 7
    print(m)

# Código principal del programa
# El ámbito de m es global
m = 5
print(m)

# Llamada a la función local()
local()
