
def somma_file(my_file, parola):
    with open(my_file, 'r') as f:
        contenuto = f.read()
    tot=0
    for line in contenuto:
        if parola in line:
            tot+=1
    return tot

def somma(file,parola):
    with open(file,'r') as file:
        tot=0
        for line in file:
            if parola in line:
                tot+=1
    return tot

 
print(somma('shampoo_sales.csv','Sales'))
