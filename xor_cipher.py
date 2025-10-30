import random

P = str(input("Ingresa el texto a cifrar: "))
C1 = len(P)

def generar_clave_binaria(longitud):
    clave = ""  
    for i in range(longitud):
        clave += str(random.randint(0, 1))
    return clave

def Encriptar(texto, clave):
    resultado = ""  
    for i in range(len(texto)):
        resultado += chr(ord(texto[i]) ^ int(clave[i % len(clave)]))
    return resultado

K = generar_clave_binaria(C1)
C = Encriptar(P, K)
To = Encriptar(C, K)

print("Clave generada: ", K)
print("Texto cifrado:", C)
print("Texto original:", To)
