import board
import player

def game(verbose):
    myBoard = board.Board()
    one = player.Random(1,myBoard)
    two = player.Random(2,myBoard)
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
        except Exception:
            print('Invalid move!')
    if(myBoard.winner>0):
        myBoard.print()
        print('Player '+str(myBoard.winner)+' wins!')
    else:
        myBoard.print()
        print('Tie game...')
    return myBoard.winner

def main():
    win = 0
    count = 0
    while(win!=-1):
        win = game(False)
        count += 1
    print('In only',count,'games, too!')
main()