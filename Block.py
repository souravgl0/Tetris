import random

Block_types=[
[[1,1,0],
 [0,1,1]],

[[1,1,1,1]],

[[1,1],
 [1,1]],

[[0,1,0],
 [1,1,1]],

[[0,1,1],
 [1,1,0]],

[[1,1,1],
 [0,0,1]],

[[1,1,1],
 [1,0,0]]
]

colors=[
(0,100,150),
(200,200,100),
(200,100,100),
(30,30,30)
]

Total_Blocks=len(Block_types)

class Block:
    def __init__(self,mid):
        blkind=random.randint(0,Total_Blocks-1)
        colind=random.randint(1,len(colors))
        self.array=Block_types[blkind]
        self.dims= [len(Block_types[blkind]) , len(Block_types[blkind][0])]
        self.crds= [ -1*self.dims[0] , mid-self.dims[1]/2]
        for i in xrange(self.dims[0]):
            for j in xrange(self.dims[1]):
                if self.array[i][j]==1: self.array[i][j]=colind

    def moveLeft(self):
        self.crds[1]-=1
    def moveRight(self):
        self.crds[1]+=1
    def moveDown(self):
        self.crds[0]+=1

    def vals_after_rotate(self):
        newDims= [self.dims[1], self.dims[0]]
        newCrds=[0,0]
        newCrds[0]=self.crds[0]+(self.dims[0]-1)/2-(newDims[0]-1)/2
        newCrds[1]=self.crds[1]+(self.dims[1]-1)/2-(newDims[1]-1)/2
        return newDims,newCrds

    def rotate(self):
        newarray=[[0 for i in xrange(self.dims[0])]
                         for j in xrange(self.dims[1])]
        rows=len(newarray)-1
        for i in xrange(self.dims[0]):
            for j in xrange(self.dims[1]):
                newarray[rows-j][i]=self.array[i][j]
        self.array=newarray
        self.dims,self.crds=self.vals_after_rotate()
