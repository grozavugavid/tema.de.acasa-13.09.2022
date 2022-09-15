def create_lista():
    n=int(input('Nr. de elemente= '))
    lista_locala=[]
    for i in range(n):
        elem=input('Elementul'+int(i)+'este:')
        lista_locala.append(elem)
    return lista_locala
lista=creare_lista()
print(lista)