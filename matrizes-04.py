#Dada a matriz [[2, 5, 9], [7, 12, 1], [6, 4, 8]], escreva um programa que encontre o maior e o menor valor presente na matriz.

matriz = [
    [2,5,9],
    [7,12,1],
    [6,4,8]
]

maior = matriz[0][0]

for linha in range (len(matriz)):
    for coluna in range (len(matriz[linha])):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]

menor = matriz [2][2]

for linha in range (len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz [linha][coluna] < menor:
            menor = matriz[linha][coluna]

print(matriz)
print(f"-->> {menor} é o menor número da matriz. ")
print (f"-->> {maior} é o maior némero da matriz. ")