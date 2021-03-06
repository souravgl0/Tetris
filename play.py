from time import sleep
from Game import Game
from Block import colors
import pygame as pyg
import sys

rows,cols=20,18
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
    scr = pyg.display.set_mode(((cols+10)*pixelMul,rows*pixelMul))
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
                    game.moveFast()
                if event.key==pyg.K_LEFT:
                    game.processInput('left')
                    leftWait=30
                if event.key==pyg.K_RIGHT:
                    game.processInput('right')
                    rightWait=30
                if event.key==pyg.K_s:
                    game.processInput('rotate')
                if event.key==pyg.K_p:
                    game.togglePause()
                if event.key==pyg.K_n:
                    if game.isGameOver():
                        del game
                        game=Game(rows,cols)
                        game.start()
            elif event.type==pyg.KEYUP and event.key==pyg.K_SPACE:
                game.moveFast(False)

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

        sidePanel=pyg.Surface((10*pixelMul,rows*pixelMul))
        sidePanel.fill((10,10,10))

        pyg.font.init()
        font=pyg.font.SysFont("Monospace",40)
        scorelbl=font.render("Score: "+str(game.score),1,(255,255,0) )

        if game.isGameOver():
            message=font.render("GAME OVER",1,(0,255,255))
            sidePanel.blit(message,(pixelMul,(rows/2)*pixelMul))
            message=font.render("Press 'n' to restart",1,(0,255,255))
            sidePanel.blit(message,(pixelMul,((rows/2)+2)*pixelMul))


        sidePanel.blit(scorelbl,(pixelMul,(rows-2)*pixelMul))
        scr.blit(sidePanel,(cols*pixelMul,0))
        pyg.display.flip()
