class Board:
    def __init__(self,x,y):
        self.rows=x
        self.cols=y
        self.array=[[0 for i in xrange(y)]
                            for i in xrange(x)]

    def checkBoardEmpty(self,a,b):
        for i in xrange(a[0],b[0]+1):
            for j in xrange(a[1],b[1]+1):
                if i>=self.rows or j>=self.cols or i<0 or j<0: return False
                if self.array[i][j]!=0: return False
        return True
    def updateBoard(self,block,crds):
        dims=[len(block),len(block[0])]
        for i in xrange(dims[0]):
            for j in xrange(dims[1]):
                if (crds[0]+i)>=0 and block[i][j]!=0: self.array[crds[0]+i][crds[1]+j]=block[i][j]
