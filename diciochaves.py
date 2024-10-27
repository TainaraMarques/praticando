#Dado o dicionário {'apple': 4, 'banana': 7, 'avocado': 2, 'berry': 6}, encontre 
#o menor valor associado a uma chave que começa com a letra "b".
def lowestvalue(dicionario):
    dicionarioB = {key: value for key, value in dicionario.items() if 'b' in key}
    lowest = min(dicionarioB.values())
    return lowest

def main():
    dicionario = {
        'apple': 4, 
        'banana': 7, 
        'avocado': 2, 
        'berry': 6
        }
    l = lowestvalue(dicionario)

    print(f"\n\n-->> Dictionary <<--\n\n{dicionario}\n\nthe lowest value associated letter b is {l}\n\n")
main()