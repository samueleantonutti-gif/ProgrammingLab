mod = -1

while (mod != 3):

    mod = input("scegliere modalità di esecuzione: \n 1 : somma di due numeri \n 2 : differenza fra due numeri \n 3 : uscire \n")
    try:
        mod = int(mod)
    except:
        print("input non valido, inserire 1, 2 o 3")
        
    if (mod not in [1, 2, 3]):
        print("numero intero non valido, inserire 1, 2, o 3")    
    
    if (mod == 1):
        a = input("inserire il primo numero")
        try:
            a = int(a)
        except:
            print("ERRORE, il primo numero deve essere intero")
        
        b = input("inserire il secondo numero")
        try:
            b = int(b)
        except:
            print("ERRORE, il secondo numero deve essere intero")
        
        print(a+b)

    elif (mod == 2):
        A = input("inserire il primo numero")
        try:
            A = int(A)
        except:
            print("ERRORE, il primo numero deve essere intero")
        
        B = input("inserire il secondo numero")
        try:
            B = int(B)
        except:
            print("ERRORE, il secondo numero deve essere intero")
        
        
        print(A-B)

    
    
