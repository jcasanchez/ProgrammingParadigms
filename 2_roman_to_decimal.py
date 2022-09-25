equivalence = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class Roman(object):
    def __init__(self, number):
        self.number = number
        self.largo = len(number)

    def roman_to_dec(self):
        sum = 0
        for x in range(0,self.largo):
            valor = equivalence[self.number[x]]
        if x != self.largo-1:
            if valor < equivalence[self.number[x+1]]:
                valor = -valor
        sum += valor
        return sum

convert = (input(Roman.roman_to_dec()))
print(convert)
