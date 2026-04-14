
def list_to_doc (mylist):
    mydoc = {}
    for element in mylist:
            if element in mydoc.keys():
                  mydoc[element]+=1
            else:
                mydoc[element]=1
    return(mydoc)
        

mylist=["casa", "mare", "casa", "casa", "albero", "mare", "mare"]
print(list_to_doc(mylist))

