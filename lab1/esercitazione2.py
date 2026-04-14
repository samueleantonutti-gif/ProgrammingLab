def compute_variations(time_series, first_year, last_year):
    mydict = {}
    
    for element in time_series: 
        
        dati = element[0].split('-')
        anno = int(dati[0]) 
        
        if element[1] == "":
            continue
        passeggeri = int(element[1])

        if anno not in mydict:
            mydict[anno] = passeggeri
        else:
            mydict[anno] += passeggeri
    
    for anno in mydict:
        mydict[anno] = mydict[anno]/12
    
    dictvalues = {}

    intervallo = last_year - first_year 

    for i in range(intervallo):
        next_year = first_year + 1

        dictvalues[f"{first_year}-{next_year}"] = mydict[next_year] - mydict[first_year]

        first_year = next_year

    return dictvalues

class CSVTimeSeriesFile :
    def __init__(self, name):
        self.name = name
    
    def get_data (self):

        listafinale = []

        with open(self.name, 'r') as f:
            next(f)
            for line in f:
                riga = line.strip().split(',')
                listafinale.append(riga)

        return listafinale

class ExamException(Exception):
    pass

time_series_file = CSVTimeSeriesFile(name = 'data.csv')
time_series = time_series_file.get_data()

#print(time_series)

print(compute_variations(time_series, 1955 , 1958))