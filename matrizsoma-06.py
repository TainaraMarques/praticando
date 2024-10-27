#Dada a matriz [[3, 8, 7], [10, 2, 5], [6, 11, 4]], escreva um programa que calcula a soma do maior valor de cada linha.
def soma(matriz):
    maior = [0][0]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] > maior:
                maior = matriz[l][c]

    seg = [0][0]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] > seg and matriz[linha][coluna] != maior:
                seg = matriz[linha][coluna]

    ter = [0][0]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if matriz[linha][coluna] > ter and matriz[linha][coluna] != maior and matriz[linha][coluna] != seg:
                ter = matriz[linha][coluna]

    soma = maior + seg + ter


    return f"Na matriz --->> {matriz} \nOs maiores valores são: {maior}, {seg} e {ter} e sua soma resulta em: {soma}"
    

def main():
    matriz = [[3, 8, 7], [10, 2, 5], [6, 11, 4]]
    s = soma(matriz)
    print (s)

main()

    
