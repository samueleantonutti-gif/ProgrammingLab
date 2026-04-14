import random

class Veicolo:
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
 
    def __str__(self):
        #2 linee di codice per il print che se no veniva una linea di 150 colonne.
 
        stringa = "Veicolo -> Marca: {}, Modello: {}, Anno: {}"
        return stringa .format(self.marca, self.modello, self.anno)
   
    def accellera(self):
        self.speed += 5
   
    def frena(self):
        self.speed -= 5
   
    def get_speed(self):
        print(self.speed)

class Macchina(Veicolo):

    def __init__ (self, anno, modello, marca, n_porte=random.randrange(2,10,2)):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
        self.n_porte=n_porte

    def __str__ (self):
        return "Veicolo -> Marca: {}, Modello: {}, Anno: {}, Numero di porte: {}".format(self.marca, self.modello, self.anno, self.n_porte)


class Moto(Veicolo):
    def __init__ (self, anno, modello, marca, n_tipo=random.randrange(0,2)):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0
        if n_tipo==1:
            self.tipo="touring"
        else:
            self.tipo="sportiva"
        

    def __str__(self):
        return "Veicolo -> Marca: {}, Modello: {}, Anno: {}, Tipo: {}".format(self.marca, self.modello, self.anno, self.tipo)
    


def vai(Veicolo):
    for i in range(10):
        Veicolo.accellera()
    Veicolo.frena()
    Veicolo.get_speed()
 
 
car = Macchina(1999, "lancer","mitsubishi",)
moto = Moto(2020, "Yamaha", "broombroom")

vai(car)
vai(moto)

print(car)
print(moto)
 

 
 