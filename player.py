import random
import board
from copy import deepcopy

class Player():
    'common base class for players'
    def __init__(self, player, board):
        if(player!=1 and player!=2):
            raise ValueError('Invalid player number.',player)
        self.player = player
        self.board = board
        
    def makeMove(self):
        raise SyntaxError('Undefined class')

class Human(Player):
    def makeMove(self):
        x = 4
        y = 4
        while x==y==4:
            coord = input('Input x,y: ')
            coord.replace(' ','')
            try:
                coordSplit = coord.split(',')
                x = int(coordSplit[0])
                y = int(coordSplit[1])
                if(0<=x<=2 and 0<=y<=2):
                    return (self.player,x,y)
                else:
                    raise ValueError('Invalid value',x,y)
            except ValueError:
                print('Valid values are 0, 1, and 2.',coord)
                x = 4
                y = 4
            except IndexError:
                print('Please enter your move.')
                x = 4
                y = 4
        return(self.player,x,y)

class Random(Player):
    def makeMove(self):
        valid = False
        while(valid==False):
            x = random.randint(0,2)
            y = random.randint(0,2)
            if(self.board.isValidMove(self.player,x,y)):
                valid = True
        return(self.player,x,y)

class Minimax(Player):
    def firstMove(self):
        copyBoard = deepcopy(self.board)
        copyBoard.makeMove(self.player,0,0)
        minloss = self.earlyMapLoss(3-self.player,copyBoard)
        minx = 0
        miny = 0
        copyBoard = deepcopy(self.board)
        copyBoard.makeMove(self.player,1,0)
        loss = self.earlyMapLoss(3-self.player,copyBoard)
        if(loss < minloss):
            minloss = loss
            minx = 1
            miny = 0
        copyBoard = deepcopy(self.board)
        copyBoard.makeMove(self.player,1,1)
        loss = self.earlyMapLoss(3-self.player,copyBoard)
        if(loss < minloss):
            minloss = loss
            minx = 1
            miny = 1
        return(self.player,minx,miny)
    
    def secondMove(self):
        minx = -1
        miny = -1
        minloss = -1
        for x in range(2):
            for y in range(x+1):
                loss = -1
                if(self.board.isValidMove(self.player,x,y)):
                    tempBoard = deepcopy(self.board)
                    tempBoard.makeMove(self.player,x,y)
                    loss += self.mapLoss(3-self.player,tempBoard)
                    if(minloss==-1):
                        minloss = loss
                        minx = x
                        miny = y
                    elif(loss < minloss):
                        minloss = loss
                        minx = x
                        miny = y
        return(self.player,minx,miny)
    
    def earlyMapLoss(self,current,copyBoard):
        if(copyBoard.winner==-1):
            return 0
        elif(copyBoard.winner==self.player):
            return 0
        elif(copyBoard.winner==(3-self.player)):
            return 1
        else:
            loss = 0
            for x in range(3):
                for y in range(x+1):
                    if(copyBoard.isValidMove(current,x,y)):
                        tempBoard = deepcopy(copyBoard)
                        tempBoard.makeMove(current,x,y)
                        loss += self.mapLoss(3-current,tempBoard)
            return loss        
    
    def mapLoss(self,current,copyBoard):
        if(copyBoard.winner==-1):
            return 0
        elif(copyBoard.winner==self.player):
            return 0
        elif(copyBoard.winner==(3-self.player)):
            return qFact(10-copyBoard.turn)
        else:
            loss = 0
            for x in range(3):
                for y in range(3):
                    if(copyBoard.isValidMove(current,x,y)):
                        tempBoard = deepcopy(copyBoard)
                        tempBoard.makeMove(current,x,y)
                        loss += self.mapLoss(3-current,tempBoard)
            return loss
        
    def makeMove(self):
        if(self.board.turn==1):
            return self.firstMove()
        if(self.board.turn==2):
            return self.secondMove()
        else:
            minx = -1
            miny = -1
            minloss = -1
            for x in range(3):
                for y in range(3):
                    loss = -1
                    if(self.board.isValidMove(self.player,x,y)):
                        copyBoard = deepcopy(self.board)
                        copyBoard.makeMove(self.player,x,y)
                        loss = self.mapLoss(3-self.player,copyBoard)
                        if(minloss==-1):
                            minloss = loss
                            minx = x
                            miny = y
                        elif(loss < minloss):
                            minloss = loss
                            minx = x
                            miny = y
        return(self.player,minx,miny)
    
def qFact(x):
    if(x==0):
        return 1
    else:
        return (x*qFact(x-1))