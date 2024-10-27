#Dada a matriz [[10, 5, 3], [6, 8, 15], [9, 2, 12]], encontre a linha que contém o maior valor da matriz e imprima essa linha.
def maior(matriz):
    maior = matriz[0][0]
    
    for linha in matriz:
        for coluna in matriz:
            maior = max(matriz)
                

        return maior
def main():
    matriz = [
        [10, 5, 3],
        [6, 8, 15], 
        [9, 2, 12]]
    
    m = maior(matriz)
    print (matriz)
    print (f"A linha q contem o maior número é: {m}")

main()