# ordena de menor a mayor variables de enteros

cont=int(input())

def llenarlista(con):
    listaNumeros=[]
    for i in range(con):
        
        numeros=int(input())
        listaNumeros.append(numeros)
        
    return listaNumeros    
listaDeNumeros=llenarlista(cont)
print(listaDeNumeros) 
print(" ")
def lista_min(lista):
    for i in range(len(lista)):
        lista.sort()
    return lista

print(lista_min(listaDeNumeros))