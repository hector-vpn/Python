def generaPares(limite):
    
    """Funcion generasPares se establece esta funcion tradicional
    para ver las diferencias con una funcion generador"""
    
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

#Llamada a la funcion tradicional.
print(generaPares(11))
print("----------------")

def generaPares2(limite):
    
    """Funcion generador"""
    num=1
    while num<limite:
        yield num*2
        num=num+1
        
#Utilizando la funcion generador        
numPares=generaPares2(11)
for i in numPares:
    print(">>",i)      

def generaPares3(limite):
    """Utilizando el metodo next accedemos a los valores del generador de uno en uno."""  
    num=1
    while num<limite:
        yield num*2
        num=num+1
        
print("---------------------------") 

numeros=generaPares3(5)
print(next(numeros))  
            
      


        
          