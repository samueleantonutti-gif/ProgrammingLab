str = input("inserire una stringa")

co_a = 0
co_e = 0
co_i = 0
co_o = 0
co_u = 0


for word in str:
    for a in word:
        co_a += 1
    for e in word:
        co_e += 1
    for i in word:
        co_i += 1
    for o in word:
        co_o += 1
    for u in word:
        co_u += 1


print(f"le a sono {co_a}, le e sono {co_e}, le i sono {co_i}, le o sono {co_o}, le u sono {co_u}")

