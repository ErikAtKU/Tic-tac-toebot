import board
from player import Human as H, Random as R, Minimax as M

def game(verbose,p1,p2):
    myBoard = board.Board()
    one = p1(1,myBoard)
    two = p2(2,myBoard)
    players = [one,two]
    current = 0
    while(myBoard.winner==0):
        if(verbose):
            myBoard.print()
            print('Player '+str(players[current].player))
        try:
            (p,x,y)=players[current].makeMove()
            myBoard.makeMove(p,x,y)
            current = (current+1)%2
        except Exception as err:
            raise(err)
    if(myBoard.winner>0):
        myBoard.print()
        print('Player '+str(myBoard.winner)+' wins!')
    else:
        myBoard.print()
        print('Tie game...')
    return myBoard.winner

def main():
    win = game(True,M,M)
main()