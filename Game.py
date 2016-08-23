from Board import Board
from Block import Block

import sys
import copy
import pygame
import threading

def addCrds(crds,delta):
    newcrds=[0,0]
    newcrds[0]=crds[0]+delta[0]
    newcrds[1]=crds[1]+delta[1]
    return newcrds

class Game:
    def __init__(self,x,y):
        self._rows=x
        self._cols=y
        self._board=Board(x,y)
        self._block=Block(x/2)
        self.score=0
        self.MoveDownInt=0.4
        self._gameRunning=True
        self._moveFast=False
        self._pause=False

    def _rotateBlock(self):
        dims,crds=self._block.vals_after_rotate()
        if self._board.checkBoardEmpty(crds, addCrds(crds,(dims[0]-1,dims[1]-1))):
            self._block.rotate()

    def _checkBlockLocked(self):
        crds=self._block.crds
        for j in xrange(self._block.dims[1]):
            i=self._block.dims[0]-1
            while self._block.array[i][j]==0: i-=1
            if crds[0]+i+1>=0 and (crds[0]+i>=self._rows-1 or self._board.array[crds[0]+i+1][crds[1]+j]!=0):
                return True
        return False

    def processInput(self,inp):
        crds,dims=self._block.crds,self._block.dims
        if inp=="left":
            if self._board.checkBoardEmpty( addCrds(crds,(0,-1)),addCrds(crds,(dims[0]-1,-1))):
                self._block.moveLeft()
        elif inp=="right":
            if self._board.checkBoardEmpty( addCrds(crds,(0,dims[1]-1+1)),addCrds(crds,(dims[0]-1,dims[1]-1+1))):
                self._block.moveRight()
        elif inp=="rotate":
            self._rotateBlock() 
        elif inp=="spaceDown":
            self._moveFast=True
        elif inp=="spaceUp":
            self._moveFast=False

    def returnState(self):
        crds=self._block.crds
        dims=self._block.dims
        rarray=copy.deepcopy(self._board.array)
        for i in xrange(crds[0],crds[0]+dims[0]):
            for j in xrange(crds[1],crds[1]+dims[1]):
                if i>=0: rarray[i][j]=self._block.array[i-crds[0]][j-crds[1]]

        return rarray

    def ContinueGame(self):
        if self._gameRunning==False:
            sys.exit()

        if not self._pause:
            self._block.crds[0]+=1

            if self._checkBlockLocked():
                self.score+=10
                self._board.updateBoard(self._block.array,self._block.crds)
                self._board.checkRowsFilled(range( self._block.crds[0] , self._block.crds[0]+self._block.dims[0] ))
                self._block=Block(self._rows/2) # new Block
                if self._checkBlockLocked():
                    print "Game Over"
                    self._gameRunning=False
                    sys.exit()
                self._moveFast=False

        if self._moveFast:
            threading.Timer(self.MoveDownInt/50,self.ContinueGame).start()
        else:
            threading.Timer(self.MoveDownInt,self.ContinueGame).start()

    def start(self):
        self.ContinueGame()

    def stop(self):
        self._gameRunning=False

    def isGameOver(self):
        return not self._gameRunning
    def pause(self):
        self._pause=not self._pause
