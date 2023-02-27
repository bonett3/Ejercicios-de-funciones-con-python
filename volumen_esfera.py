#calcula el volumen de una esfera

radio=float(input())
pi=3.14159

def volumenEsfera(p,r):
    volumen=p*(r**2)
    return volumen

resultadoVolumen=volumenEsfera(pi,radio)

print("%.2f" % resultadoVolumen)
