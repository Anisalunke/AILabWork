# board formation
def Board(board):
    print("Current State Of Board : \n\n")
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):    
            print("X ",end=" ")
    print("\n\n")

# player turns (X and O)
def player1Turn(board):
    print("Player 1's turn")
    pos=input("Enter X's position from [1...9]: ")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move!!!")
        exit(0) 
    board[pos-1]=-1

def player2Turn(board):
    print("Player 2's turn")
    pos=input("Enter O's position from [1...9]: ")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move!!!")
        exit(0)
    board[pos-1]=1

# checks the result of the game
def boardanalyser(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

def minimax(board,player):
    x=boardanalyser(board)
    if(x!=0):
        return (x*player)
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minimax(board,(player*-1))
            if(score>value):
                value=score
                pos=i
            board[i]=0

    if(pos==-1):
        return 0
    return value

# computer player
def computer(board):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board, -1)
            board[i]=0
            if(score>value):
                value=score
                pos=i
 
    board[pos]=1

def main():
    choice=input("Enter 1 for single player, 2 for multiplayer: ")
    choice=int(choice)
    board=[0,0,0,0,0,0,0,0,0]
    if(choice==1):
        print("Computer : O Vs. You : X")
        player= input("Enter to play 1(st) or 2(nd) :")
        player = int(player)
        for i in range (0,9):
            if(boardanalyser(board)!=0):
                break
            if((i+player)%2==0):
                computer(board)
            else:
                Board(board)
                player1Turn(board)
    else:
        for i in range (0,9):
            if(boardanalyser(board)!=0):
                break
            if((i)%2==0):
                Board(board)
                player1Turn(board)
            else:
                Board(board)
                player2Turn(board)
    x=boardanalyser(board)
    if(x==0):
         Board(board)
         print("Draw!!!")
    if(x==-1):
         Board(board)
         print("X Wins!!! Y Loose !!!")
    if(x==1):
         Board(board)
         print("X Loose!!! O Wins !!!!")
       
main()
