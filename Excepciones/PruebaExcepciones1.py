def suma(a,b):
    resultado=a+b
    return resultado

def resta(a,b):
    resultado=a-b
    return resultado

def multiplicacion(a,b):
   resultado=a*b
   return resultado

def division(a,b):
    try:
        resultado=a/b
    except ZeroDivisionError:   
        print("No se puede dividir entre cero")
        return "Error...!"
    return resultado
while True:
    try:
        num1=int(input(">> "))
        num2=int(input(">> "))
        break
    except ValueError:
        print("Error.. solo se admiten valores numericos.")

op=input("""Ingrese operacion a realizar:
         -Suma
         -Resta
         -Multiplicacion
         -Division 
         >>""")
op2=op.lower()

if op2=="suma":
    print(suma(num1,num2))
elif op2=="resta":
    print(resta(num1,num2))
elif op2=="multiplicacion":
    print(multiplicacion(num1,num2))
elif op2=="division":
    print(division(num1,num2))   
else:
    print("ERROR..!")       
    
print("Continua la ejecucion")          