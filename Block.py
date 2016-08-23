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

Total_Blocks=len(Block_types)

class Block:
    def __init__(self,mid):
        ind=random.randint(0,Total_Blocks-1)
        self.array=Block_types[ind]
        self.dims= [len(Block_types[ind]) , len(Block_types[ind][0])]
        self.crds= [ -1*self.dims[0] , mid-self.dims[1]/2]

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
