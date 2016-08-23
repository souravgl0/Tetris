class Board:
    def __init__(self,x,y):
        self.rows=x
        self.cols=y
        self.array=[[0 for i in xrange(y)]
                            for i in xrange(x)]
        for i in xrange(5):
            for j in xrange(x):
                self.array[j][i]=1
        # for i in xrange(x-1,x-5,-1):
            # self.array[i]=[1 for j in xrange(y)]

    def checkBoardEmpty(self,a,b):
        for i in xrange(a[0],b[0]+1):
            for j in xrange(a[1],b[1]+1):
                if i>=self.rows or j>=self.cols: return False
                if self.array[i][j]==1: return False
        return True
    def updateBoard(self,block,crds):
        dims=[len(block),len(block[0])]
        for i in xrange(dims[0]):
            for j in xrange(dims[1]):
                if block[i][j]==1: self.array[crds[0]+i][crds[1]+j]=block[i][j]
