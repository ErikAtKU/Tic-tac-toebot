class Board():
    'Defining the board and valid moves'
    def __init__(self):
        self.board = [0,0,0,0,0,0,0,0,0]
        self.turn = 1
        self.winner = 0
        
    def isValidMove(self,player,x,y):
        pos = (3*y) + x
        if(self.board[pos]==0):
            return True
        else:
            return False
    
    def makeMove(self,player,x,y):
        if(self.winner==0):
            if(self.turn%2 == player%2):
                if(self.isValidMove(player,x,y)):
                    self.board[(3*y)+x]=player
                    self.turn += 1
                    self.isWin()
                    if(self.turn==10 and self.winner==0):
                        self.winner=-1
                else:
                    raise IndexError('Invalid move!','Player '+str(player)+' tried to move to',x,y)
            else:
                raise ValueError('Invalid turn order!','Player '+str(player)+' tried to move')
        else:
            raise StopIteration('The game is finished!','Player '+str(self.winner)+' won!')
        
    def print(self):
        printBoard = ['X' if x == 1 else 'O' if x == 2 else '-' for x in self.board]
        print('Turn: '+str(self.turn-1))
        print('  0 1 2')
        print('0|'+str(printBoard[0])+'|'+str(printBoard[1])+'|'+str(printBoard[2])+'|')
        print('1|'+str(printBoard[3])+'|'+str(printBoard[4])+'|'+str(printBoard[5])+'|')
        print('2|'+str(printBoard[6])+'|'+str(printBoard[7])+'|'+str(printBoard[8])+'|')
    
    def isWin(self):
        board = self.board
        if( 1==board[0]==board[1]==board[2] or \
            1==board[3]==board[4]==board[5] or \
            1==board[6]==board[7]==board[8] or \
            1==board[0]==board[3]==board[6] or \
            1==board[1]==board[4]==board[7] or \
            1==board[2]==board[5]==board[8] or \
            1==board[0]==board[4]==board[8] or \
            1==board[2]==board[4]==board[6] or \
            1==board[6]==board[7]==board[8] ):
            self.winner = 1
        if( 2==board[0]==board[1]==board[2] or \
            2==board[3]==board[4]==board[5] or \
            2==board[6]==board[7]==board[8] or \
            2==board[0]==board[3]==board[6] or \
            2==board[1]==board[4]==board[7] or \
            2==board[2]==board[5]==board[8] or \
            2==board[0]==board[4]==board[8] or \
            2==board[2]==board[4]==board[6] or \
            2==board[6]==board[7]==board[8] ):
            self.winner = 2