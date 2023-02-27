# Halla el valor maximo que se encuentre en una lista de enteros

cantidad=int(input())
listaNumeros=[]

for i in range(cantidad):
    numeros=float(input())
    listaNumeros.append(numeros)

def maximo(lista):
    cont=1
    for i in range(cont):
     maxima=max(lista)
    return maxima
       
resultadoMaximo=maximo(listaNumeros)    
print(resultadoMaximo)



