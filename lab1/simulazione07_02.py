class ExamException(Exception):
    pass

def compute_variations (lista, inizio, fine, n):
    
    if n > fine-inizio:
        raise ExamException ("la finestra deve essere strettamente minore dell'intervallo")
    
    diztmp = {}

    for element in lista:

        anno = int(element[0].split('/')[0])

        if (inizio <= anno <= fine) :
            if anno not in diztmp:
                diztmp[anno] = [float(element[1])]
            else:
               diztmp[anno].append(float(element[1]))
    

    dizmedie = {}

    for chiave in diztmp:
        dizmedie[chiave] = sum(diztmp[chiave])/len(diztmp[chiave])

    
    dizmediemobili = {}

    for chiave in dizmedie:
        dizmediemobili[chiave] = 0
        if chiave - n >= inizio:
            for j in range(1, n+1):
                dizmediemobili[chiave] += dizmedie[chiave-j]
        
        dizmediemobili[chiave] = dizmediemobili[chiave]/n


    dizfinale = {}

    for chiave in dizmediemobili :
        if dizmediemobili[chiave] == 0.0 :
            dizmediemobili[chiave] = 0.0
        else:
            dizfinale[str(chiave)] = dizmedie[chiave] - dizmediemobili[chiave]
    

    return dizfinale


class CSVTimeSeriesFile :
    def __init__(self, name):

        self.name = name 

        try:
            file = open(self.name)
            file.close()

        except :
            raise ExamException(f"Il file {self.name} che stai cercando di aprire, non esiste")



    def get_data(self):
        lista_dati = []
        with open (self.name, 'r') as f:
            
            next(f)

            for line in f:

                rigapulita = line.strip().split(',')

                if len(rigapulita) <2 or rigapulita[1] == "":
                    continue

                try:
                    valore = float(rigapulita[1])
                except:
                    continue

                if valore < 0 :
                    continue

                riga_dati = [rigapulita[0], valore]

                lista_dati.append(riga_dati)

        return(lista_dati)
    

    
time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
#print(time_series)

dizionario = compute_variations(time_series, 1900, 1904, 3)

print(dizionario)