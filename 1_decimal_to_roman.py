roman_symbol = [['I','V','X'],['X','L','C'],['C','D','M']]
popurri = {0:'',1:'0',2:'00',3:'000',4:'01',5:'1',6:'10',7:'100',8:'1000',9:'02'}

class roman(object):
    def __init__(self, number):
        self.number = str(number)
        self.lenght = len(self.number)

    def dec_to_roman(self):
        result = ''
        for x in range(0,self.lenght):
            result = result + self.dec_to_romandig(self.number[x],self.lenght-x-1)
            return result

    def dec_to_romandig(self,digito,categoria):
        logica = roman_symbol[categoria]
        answer = ''
        dig_a_procesar = [x for x in popurri[int(digito)]]
        for x in dig_a_procesar:
            answer = answer + logica[int(x)]
            return answer

Prueba = input(roman())
print(Prueba.dec_to_roman())
