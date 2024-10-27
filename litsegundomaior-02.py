#Dada a lista [7, 12, 22, 5, 9, 34], escreva um programa que encontre o segundo maior valor da lista.
lista = [7,12,22,5,9,34]

maior = max(lista)

lista_sem_maior = [x for x in lista if x != maior]
seg_maior = max(lista_sem_maior)
print(f"{seg_maior} é o segundo maior número da lista. ")