players_dtl={}
from IPython.display import clear_output
from random import randint
def players_details():
    clear_output()
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    p1_name = input("Enter the first player name ")
    p2_name = input("Enter the second player name ")
    p1_marker ='N'
    while p1_marker not in (['X','O']):
        p1_marker=input("choose the first player marker out of X|O ")
    if p1_marker.upper() == 'X':
        p2_marker='O'
    else:
        p2_marker='X'

    players_dtl={'p1_name':p1_name,'p2_name':p2_name,'p1_marker':p1_marker,'p2_marker':p2_marker}

    print(p1_name+' choose '+p1_marker+ ' marker.')
    print( p2_name + ' choose ' + p2_marker + ' marker.')
    #-------------------toss
    print("Are you ready for the toss ? (yes|no)")
    ready_for_toss=input()
    if ready_for_toss.upper()=='YES':
        ts = randint(1, 2)
        who_won_toss = ''
        if ts == 1:
            print(players_dtl['p1_name'] + ' has won the toss')
            who_won_toss = players_dtl['p1_name']
        else:
            print(players_dtl['p2_name'] + ' has won the toss')
            who_won_toss = players_dtl['p2_name']
    else:
        pass

    if who_won_toss == p1_name:
        first_marker=players_dtl['p1_marker']
    else:
        first_marker = players_dtl['p2_marker']

    #def game_board(board,position,marker):
    while ' ' in board:
        clear_output()
        print("choose the position: ")
        pos = int(input())
        if board[pos]==' ':
            board[pos]=first_marker
        else:
            print("You can not choose already filled position")
            continue
        print(board[7] + ' | ' + board[8] + ' | ' + board[9] )
        print('-'*9)
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-'*9)
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])

        # code to check who win on each iteration
        if (''.join(board[1:4])==first_marker*3 or ''.join(board[4:7])==first_marker*3 or ''.join(board[7:])==first_marker*3 or
            board[1]==board[4]==board[7]==first_marker or board[2]==board[5]== board[8]==first_marker or
             board[3] == board[6] == board[9] == first_marker or board[1]== board[5]==board[9]==first_marker or
             board[7] == board[5] == board[3] == first_marker):

            for k,v in players_dtl.items():
                if v==first_marker:
                    player_won=str(k)[0:2]+'_name'
                    print('player '+ players_dtl[player_won] + ' has won')
            break
        if first_marker == 'X':
            first_marker = 'O'
        else:
            first_marker = 'X'

players_details()

