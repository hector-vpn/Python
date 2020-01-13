class vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.en_marcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.acelera=True
        
    def acelerar(self):
        self.acelera=True   
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("""Marca: {}
Modelo: {}
En Marcha: {}
Acelerando: {}
Frenando: {}""".format(self.marca,self.modelo,self.en_marcha,self.acelera,self.frena))            
        
class Moto(vehiculos):
    
    caballito=""
    
    def willy(self):
        
        self.caballito="Voy haciendo willy"

    def estado(self):
        print("""Marca: {}
Modelo: {}
En Marcha: {}
Acelerando: {}
Frenando: {}
{}""".format(self.marca,self.modelo,self.en_marcha,self.acelera,self.frena,self.caballito))   
        
class Furgoneta(vehiculos):
    
    def carga(self,cargar):
        self.cargado=cargar 
        if(self.cargado):
            return "La Furgoneta esta cargada"
        else:
            return "La Furgoneta esta vacia"       
        
miMoto=Moto("Honda","CBR")
miMoto.willy()
miMoto.estado()  

miFurgoneta=Furgoneta("Renault","Kangoo")   
miFurgoneta.arrancar()
print(miFurgoneta.carga(True))
miFurgoneta.estado() 