import random
import board

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

class Gametree(Player):
    def makeMove(self):
        'lol'