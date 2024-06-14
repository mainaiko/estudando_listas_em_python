# frutas = ["laranja", "maca", "uva"]
# print (frutas[-3])

# frutas = []
# print (frutas)

# letras = list("python")
# print (letras)

# numeros = list(range(10))
# print (numeros)

# carro = ["Ferrari", "F8", 4.200000, 2020, 2900, "Brasilia", True ]
# print (carro[0], carro[4])

# matriz = [
#     [1, "a", 2],
#     ["b", 3, 4],
#     [6, 5, "c"]
# ]

# print (matriz[0])
# print (matriz[0][0])
# print (matriz[0][-1])
# print (matriz[-1][-1])


# carros = ["up", "mobi", "civic"]

# # for carro in carros:
# #     print (carro)

# for indice, carro in enumerate(carros):
#     print (f"{indice}: {carro}")

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros: 
    if numero % 2 == 0: # se a sobra da divisao for igual a zero é um numero par
        pares.append (numero)
print (pares)


