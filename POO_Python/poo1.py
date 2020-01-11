class Coche():
    def __init__(self):
        self.__largo_chasis=250
        self.__ancho_chasis=120
        self.__ruedas=4
        self.__en_marcha=False
    
    def arrancar(self,arrancamos):
        self.__en_marcha=arrancamos
        
        if(self.__en_marcha):
            chequeo=self.__checkup()
            
        if(self.__en_marcha and chequeo ):
            return "El coche esta en marcha.."
        elif (self.__en_marcha and chequeo==False):
            return "Algo esta mal verifica los indicadores" 
        else:
            return "El coche esta apagado.."   
    
    def estado(self):
      print("""El largo del coche es {}cm
El coche tiene {} ruedas y un ancho de {}cm """.format(self.__largo_chasis, self.__ruedas,self.__ancho_chasis))
      
    def __checkup(self):
        print("Realizando chequeo interno..!")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
           return False
          
coche1=Coche()   

print(coche1.arrancar(True))
coche1.estado()