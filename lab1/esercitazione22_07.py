class ExamException(Exception):
    pass

def compute_month_variation(time_series, first_year, second_year):
    
    if not isinstance(first_year, int) or not isinstance(second_year, int):
        raise ExamException('Errore: gli anni inseriti devono essere di tipo intero.')
    if first_year >= second_year:
        raise ExamException('Errore: il secondo anno deve essere maggiore del primo')

    diztemp1 = {}
    
    for element in time_series:
        
        datacompleta = element[0].split('/')
        anno = int(datacompleta[2])
        mese = int(datacompleta[1])
        
        if anno == first_year:
            if anno not in diztemp1:
                diztemp1[anno] = {}
        
            diztemp1[anno][mese] = element[1]

    diztemp2 = {}
    
    for element in time_series:
        
        datacompleta = element[0].split('/')
        anno = int(datacompleta[2])
        mese = int(datacompleta[1])
        
        if anno == second_year:
            if anno not in diztemp2:
                diztemp2[anno] = {}
        
            diztemp2[anno][mese] = element[1]

    dizdiff = {}

    for mese in diztemp2[second_year]:
        if mese in diztemp1[first_year]:
            dizdiff[mese] = diztemp2[second_year][mese] - diztemp1[first_year][mese]
        else:
            print(f"La variazione per il mese {mese} non può essere calcolata")
        
    if dizdiff == {}:
        raise ExamException('Gli anni considerati non hanno mesi validi')

    return dizdiff   

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
        try:
            file = open(self.name)
            file.close()
        except:
            raise ExamException('Errore : Impossibile aprire il file!')
        

    def get_data(self):

        listafinale = []

        with open(self.name, 'r') as f:
            next(f)

            for line in f:
                riga = line.strip().split(',')
                if int(riga[2]) < 5:
                    rigadati = [riga[0], float(riga[1])]
                    listafinale.append(rigadati)
                else:
                    print("Data saltata perchè valore troppoincerto")

        return listafinale
