#inverte el orden una cadena de variables que se digite

cont=int(input())
def llenarLista(C):
    listaCadena=[]
    for i in range(0,C):
        nombres=input()
        listaCadena.append(nombres)
    return listaCadena    
resultadoLista=llenarLista(cont)    

def invertir(lista):
    newlist=[]
    newlist=lista[::-1]
    return newlist  


listaInversa=invertir(resultadoLista)

print(listaInversa)