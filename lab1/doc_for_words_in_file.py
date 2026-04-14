def crea_diz (file):
    mydoc = {}
    with open(file, 'r') as file:

        next(file)

        for line in file:

            riga = line.split(',')

            for element in riga:

                if element in mydoc:
                    mydoc[element]+=1

                else:
                    mydoc[element]=1


    return(mydoc)

myfile = "shampoo_sales.csv"
dizionario = crea_diz(myfile)
print(f"{dizionario}")