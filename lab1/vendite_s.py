def somma_vendite (file):
    sum = 0.0
    with open (file, 'r') as file:

        next(file)                                 #saltiamo l'headliner

        for line in file:
            rigapulita = line.split(',')
            sum += float(rigapulita[1])

    return (sum)

somma = somma_vendite("shampoo_sales.csv")
print(somma)
