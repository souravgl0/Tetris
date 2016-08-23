from time import sleep
from Game import Game
from Block import colors
import pygame as pyg
import sys

rows,cols=30,32
pixelMul=30
bgCol=(51,51,0)

def draw_rect(surface, fill_color, outline_color, rect, border=1):
    surface.fill(outline_color, rect)
    surface.fill(fill_color, rect.inflate(-border*2, -border*2))

def RenderBoard(surface,array):
    N=len(array)
    M=len(array[1])
    for i in xrange(N):
        for j in xrange(M):
            if array[i][j]!=0:
                draw_rect(surface,colors[array[i][j]-1],bgCol,pyg.Rect(j*pixelMul,i*pixelMul,pixelMul,pixelMul))

if __name__ == "__main__":
    scr = pyg.display.set_mode((cols*pixelMul,rows*pixelMul))
    game=Game(rows,cols)
    game.start()
    while(1):
        events=pyg.event.get()
        for event in events:
            if event.type == pyg.QUIT:
                game.stop()
                sys.exit()
            elif event.type==pyg.KEYDOWN:
                if event.key==pyg.K_SPACE:
                    game.processInput("spaceDown")
                if event.key==pyg.K_LEFT:
                    game.processInput('left')
                    leftWait=30
                if event.key==pyg.K_RIGHT:
                    game.processInput('right')
                    rightWait=30
                if event.key==pyg.K_s:
                    game.processInput('rotate')
            elif event.type==pyg.KEYUP and event.key==pyg.K_SPACE:
                game.processInput("spaceUp")

        keys=pyg.key.get_pressed()
        if keys[pyg.K_LEFT]:
            if leftWait==0: game.processInput('left')
            else: leftWait-=1
        if keys[pyg.K_RIGHT]:
            if rightWait==0: game.processInput('right')
            else: rightWait-=1

        sleep(0.01)
        scr.fill(bgCol)
        RenderBoard(scr,game.returnState())
        pyg.display.flip()

#------------------------------
