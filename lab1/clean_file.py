def clean (file):

    righe_viste = set()

    with open (file) as f:
        newfile = open("unique.txt", 'x')
        for line in f:
            if line in righe_viste:
                continue
            else:
                righe_viste.add(line)
                newfile.write(line)
        
        newfile.close()
    return(0)



myfile = "shampoo_sales.csv"
clean(myfile)