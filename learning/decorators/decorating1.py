
def checkMatrix(func):
    def check(matrix1, matrix2):
        if len(matrix1.matrix) != len(matrix2.matrix):
            raise ValueError
    
        elif len(matrix1.matrix[0]) != len(matrix2.matrix[0]):
            raise ValueError
        else:
            # it seems that we need to run the 
            # passed function this way. 
            # i.e. when we decorate, it is simply
            # a substitute for making code more
            # readable and easier to write
            func(matrix1, matrix2)
    return check
        


class Matrix:
    def __init__(self, Rows, Columns):
        print("matrix")
        self.rows = Rows
        self.cols = Columns
        self.matrix = []
        
        for i in range(self.rows):
            col = self.cols * [0]
            self.matrix.append(col)

    @checkMatrix
    def add(self, matrix2):
        print("added")
    
    @checkMatrix
    def sub(self,matrix2):
        print("subtracted"):