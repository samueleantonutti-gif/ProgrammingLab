class Canguro:
    def __init__(self, contenuto_tasca=[]):     
        self.contenuto_tasca=contenuto_tasca
    
    def intasca(self, obj):                         #metodo che aggiunge un oggetto alla tasca
        self.contenuto_tasca.append(obj)
    
    def __str__ (self):                                                     #metodo che cambia il modo in cui stampo la classe
        return "Canguro con in tasca {}".format(self.contenuto_tasca)
    
can=Canguro()
guro=Canguro()

can.intasca("figlio")         #aggiungo a can oggetti
can.intasca("macchina")

print(can)
print(guro)                   #guro ha gli stessi elementi di can, perchè?
                              #perchè la lista istanziata nella lista della classe è la stessa per qualsiasi oggetto

                              #posso risolvere usando @classmethod
                              
                              #oppure con
# def __init__(self, contenuto_tasca=None):     
#     if contenuto_tasca is None:
#         self.contenuto_tasca = []
#     else:
#         self.contenuto_tasca = contenuto_tasca
            
