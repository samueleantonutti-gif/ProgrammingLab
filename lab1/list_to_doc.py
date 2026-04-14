list = ["ciao", "bello", "io", "ciao", "ciao", "miao", "non", "io", "addirittura"]

doc = {}

for element in list:
    if element not in doc:
        doc[element] = 1
    else :
        doc[element] += 1

print(doc)

