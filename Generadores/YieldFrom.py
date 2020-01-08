"""El (*) delante del parametro nos indica que la funcion recibira un nro 
indeterminado de parametros y ademas los recibira en forma tupla."""
print("Ejemplo n°1")
def  Ciudades(*city):
    for i in city:
        for j in i:
            yield j

capitales=Ciudades("Buenos Aires","Londres","Madrid","Lima","Montevideo","Lisboa","Washintong DC","Mexico DF","La Havana","Medellin")

print(next(capitales))        
print(next(capitales))   
print("-----------------\nEjemplo n°2")
def Nombres(*name):
    """La instruccion yield from nos permite acceder a subelementos de una
     forma mas sencilla evitando el uso de bucles anidados"""
    for i in name:
        yield from i
        
nombre=Nombres("hector","Horacio")
print(next(nombre))
print(next(nombre))        