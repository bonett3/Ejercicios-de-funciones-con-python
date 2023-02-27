# calcula el factorial de cualquier numero entero
numero=int(input())

def factorial(num):
    
    for i in range(1,num):
        num*=i
        
    return num

resultadoFatorial=factorial(numero)

print(resultadoFatorial)