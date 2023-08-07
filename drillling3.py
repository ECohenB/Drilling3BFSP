nombres = [
    'Harry Houdini',
    'Newton',
    'David Blaine',
    'Hawking',
    'Messi',
    'Teller',
    'Einstein',
    'Pele',
    'Juanes'
]

# 1.- Separar los nombres en tres grupos: magos, científicos y otros:
magos = []
cientificos = []
otros = []

for nombre in nombres:
    if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
        magos.append(nombre)
    elif nombre in ['Newton', 'Hawking', 'Einstein']:
        cientificos.append(nombre)
    else:
        otros.append(nombre)

# 2. Definir una función para hacer magos grandiosos
def hacer_grandioso(nombres):
    return [f'El gran {nombre}' for nombre in nombres]

magos_grandiosos = hacer_grandioso(magos)

# 3. Crear función para imprimir los nombres
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# 4.Imprimir la lista completa de nombres antes de ser modificados
print('Lista completa de nombres:')
imprimir_nombres(nombres)

# 5. Imprimir los nombres de los magos grandiosos
print('Magos grandiosos:')
imprimir_nombres(magos_grandiosos)

# Imprimir los nombres de los científicos
print('Científicos:')
imprimir_nombres(cientificos)

# Imprimir los nombres restantes
print('Otros:')
imprimir_nombres(otros)