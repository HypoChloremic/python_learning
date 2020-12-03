class Test:
    def __init__(self):
        self.list = [0,10,20]
    
    def __getitem__(self, ind):
        return self.list[ind]


if '__main__' == __name__:
    c = Test()
    print(c[1])