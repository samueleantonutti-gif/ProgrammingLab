#programma che chiede all'utente di inserire un numero e ne stampa il quadrato e il cubo

def eleva_al_quadrato (num):
    quad= num * num
    return quad

def eleva_al_cubo (num):
    cubo= num * num * num
    return cubo


num = int(input("inserire numero da elevare al quadrato e al cubo"))
quad1 = eleva_al_quadrato(num)
cub1 = eleva_al_cubo(num)
print(quad1)
print(cub1)

