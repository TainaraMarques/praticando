#Dado o dicionário {'x': 4, 'y': 19, 'z': 8, 'w': 11}, calcule a diferença entre o maior e
# o menor valor e imprima o resultado

def maior(dicionario):
    maior = max(dicionario.values())
    return maior

def menor(dicionario):
    menor = min(dicionario.values())
    return menor

def diferença(dicionario):
    ma = maior(dicionario)
    me = menor(dicionario)
    diferença = ma - me
    return f"O menor e o maior número são {me} e {ma} e diferença entre eles é {diferença}\n\n"

def main():
    dicionario = {
        'x': 4, 
        'y': 19, 
        'z': 8, 
        'w': 11
    }

    d = diferença(dicionario)

    print(f"\n\n-->> Dicionário {dicionario}\n\n{d}")

main()