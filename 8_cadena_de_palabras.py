class Reverse(object):

    def __init__(self, strString):
        self.strString = strString
        self.list_String = self.strString.split(" ")
        self.newString = []

    def reverse(self):
        for i in range( 0, len(self.list_String) ):
            self.newString.append(self.list_String[(i+1) * -1] )
            self.newString = ' '.join(self.newString)

    def __str__(self):
        return "Entrada: {0}. Salida: {1}.".format(self.strString, self.newString)

if __name__ == '__main__':
    r = Reverse("Mi Diario Python")
    r.reverse()
print(str(r))
