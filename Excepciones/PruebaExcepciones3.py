import math

def raiz_cuadrada(num):
    if num<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num)
    
op1=int(input(">>Ingrese un numero: "))    

try:
    print(raiz_cuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Fin de la ejecucion...!")        
    