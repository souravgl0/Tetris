import os
from time import sleep
from Game import Game

game=Game(30,32)


#--------------- temp- for testing
while(1):
    sleep(0.05)
    # os.system('clear')
    game.process()
    game.printBoard()

#------------------------------
