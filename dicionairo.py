#Dado o dicionário {'a': 10, 'b': 3, 'c': 15, 'd': 7}, encontre a chave que possui o maior valor e imprima-a.
def maior(dicionario):
    maior = max(dicionario)

    return maior

def main():
    dicionario ={
    'a': 10, 
    'b': 3, 
    'c': 15, 
    'd': 7
}
    
    m = maior(dicionario)

    print (f"\n\n-->> Dicionário:  {dicionario} \n\nO maior número presente no dicionario é {m}\n\n")

main()