class Board:
    def __init__(self,x,y):
        self.rows=x
        self.cols=y
        self.array=[[0 for i in xrange(y)]
                            for i in xrange(x)]

    def checkBoardEmpty(self,a,b , arrayToFit=None):
        for i in xrange(a[0],b[0]+1):
            for j in xrange(a[1],b[1]+1):
                if i>=self.rows or j>=self.cols or i<0 or j<0: return False
                if arrayToFit!=None and arrayToFit[i-a[0]][j-a[1]]==0: continue
                if self.array[i][j]!=0: return False
        return True

    def updateBoard(self,block,crds):
        dims=[len(block),len(block[0])]
        for i in xrange(dims[0]):
            for j in xrange(dims[1]):
                if (crds[0]+i)>=0 and block[i][j]!=0: self.array[crds[0]+i][crds[1]+j]=block[i][j]

    def _deleteRow(self,row):
        newArray=[[0 for i in xrange(self.cols)] ]+ self.array[:row]+self.array[row+1:]
        self.array=newArray

    def checkRowsFilled(self,rows):
        for row in rows:
            filled=True
            for i in xrange(self.cols):
                if self.array[row][i]==0:
                    filled=False
                    break
            if(filled):self._deleteRow(row)

