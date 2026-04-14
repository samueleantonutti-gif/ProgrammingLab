from copy import copy

class fileCSV ():
    
    def __init__(self, name):
        self.name=name
    
    def get_data(self, start=None, end=None):
        """
        Il metodo si occupa di leggere un file CSV e di creare una lista di liste in cui sono
        rappresentate tutte le righe del file, separando la data dal valore. La funzione ritorna
        tale lista di liste

        se vengono specificati start e end, legge solo le righe comprese nell'intervallo richiesto
        """
        lista_dati=[]
        if (isinstance(start, int) or isinstance(end, int)):
            if(start <= end):
                if (0< start < 40 and 0< end < 40):
                    try:
                        file = open(self.name, 'r')
        
                        for i, line in enumerate(file):
                            if i>=start and i<=end:
                                lista_interna = line.strip().split(',')
                                lista_dati.append(lista_interna)
                            file.close()
                        return(lista_dati)
            
                    except FileNotFoundError:
                        return(f"Il file {self.name} che stai cercando di aprire, non esiste")
                else:
                    print(f"start e end non sono nel range di righe del file {self.name}")    
            else:
                print("start deve essere minore di end")        
        else:
            print("non sono stati rilevati interi nei parametri start e end")



        lista_finale=copy(lista_dati)
        try:
            file = open(self.name, 'r')
        
            for line in file:   #in questo for creaiamo le liste che comporranno la lista di ritorno.
                # con lo strip rimuoviamo i caratteri di default "\n" inutile ai fini del controllo dati
                # con lo split invece ci occupiamo di dividere data dal dato.
            
                lista_interna = line.strip().split(',')
                lista_finale.append(lista_interna)
                #print(line)
            file.close()
            return(lista_finale)
            
        except FileNotFoundError:
            return(f"Il file {self.name} che stai cercando di aprire, non esiste")
        
class NumericalCSVFile(fileCSV):

    def __init__(self,name):
        super().__init__(name)
        self.data=self.converti_infloat()
        
    def converti_infloat(self):
        
        lista_float = []
        try: 
            with open(self.name, 'r') as file:

                for line in file:  
                    # per ogni riga ripete questo processo:
                                                                                      
                    elemento_di_lista = line.strip().split(',')  

                    # trasforma la riga in un "elemento" lista composto da data e numero, entrambi come stringa
                                                     
                    riga_nuova = [elemento_di_lista[0]] + [float(x) for x in elemento_di_lista[1:]]

                    # crea una nuova riga, come somma di liste, cioè data + numero castato a float
                    # (dobbiamo usare x come variabile per indicare la stringa in posizione di indice 1 nella lista che è la riga)

                    lista_float.append(riga_nuova)

                    # appendiamo la nuova riga alla nostra lista con i dati come li vogliamo noi

            return lista_float
        
        except FileNotFoundError:
            print(f"Errore: File {self.name} non trovato.")
            return []   
 
vendite_shampoo_file = NumericalCSVFile('shampoo_sales.csv')
print(vendite_shampoo_file.data)