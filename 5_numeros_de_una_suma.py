class Peers(object):
    list_Numbers = [10, 20, 10, 40, 50, 60, 70]

    def __init__(self, int_Obj):
        self.int_Obj = int_Obj

    def findPeers(self):
        for i in range(len(self.list_Numbers)):
            if (self.list_Numbers[i] + self.list_Numbers[i - 1]) == self.int_Obj:
                self.i = i
        self.i_1 = (i-1)

    def __str__(self):
        return ("Los Indices que Suman {0} son ({2}, {1}).".format(self.int_Obj, self.i, self.i_1))

if __name__ == '__main__':
    peers = Peers(50)
    peers.findPeers()
print(str(peers))
