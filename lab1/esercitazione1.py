class MovingAverage :
    def __init__ (self, n):
        if not isinstance(n, int) or n <= 0:
            raise ExamException('La finestra deve essere un intero postivo!')
        self.finestra = n

    def compute (self, lista):

        """
        questo metodo si occupa di calcolare la media mobile per una lista, la finestra di tale media mobile 
        deve essere specificata in input
        """
        
        #prima gestisco l'input
        if not isinstance(lista, list) :
            raise ExamException('inserire una lista')
        for element in lista:
            if not isinstance(element, (int, float)):
                raise ExamException('la lista deve contenere numeri')
            
        if lista == []:
            raise ExamException('Errore, lista valori vuota!')
        

        if len(lista) < self.finestra :
            raise ExamException('Errore, la lista non può avere meno elementi della linghezza della finestra!')
        

        listafinale = []
        for i in range(len(lista) - self.finestra + 1):
            lista_tmp = lista[i:i+self.finestra]
            
            media = sum(lista_tmp) / self.finestra

            listafinale.append(media)

        return(listafinale)
    
class ExamException(Exception):
    pass

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)