# devuelve una lista de nombres de forma ordenada alfabeticamente 

contador=int(input())
listaNombres=[]
for i in range(contador):
    nombres=input()
    listaNombres.append(nombres)

def nombre(list):
    newlist=[]
    cont=1
    for i in range(0,cont):
        newlist=sorted(list)
    return newlist 

result=nombre(listaNombres)
print(result)