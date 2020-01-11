def div():
    while True:
        try:
            num1=int(input(">> "))
            num2=int(input(">> "))
            print(">>",num1/num2)
            break
        except ZeroDivisionError:
            print("No se puede dividir por cero") 
        except ValueError:
            print("Error..! debe ingresar valores numericos")   
        finally:
            
            """Todas las instrucciones que se encuentren dentro
               del finally se ejecutaran siempre """        
               
            print("Calculo finalizado..")    

div()        