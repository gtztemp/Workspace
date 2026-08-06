""" Tic Tac Toe
----------------------------------------
"""
import random

# Initialize board (0-8)
board = [i for i in range(9)]
player, computer = '', ''

# Move priorities: Corners, Center, Others
moves = ((0, 2, 6, 8), (4,), (1, 3, 5, 7))

# Winner combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), 
           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = '\n'
            if i != 2 and i != 5 and i != 8: 
                end += '---------\n'
        char = str(i) if isinstance(i, int) else i
        x += 1
        print(char, end=end)

def select_char():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if 0 <= move < 9 and isinstance(brd[move], int):
        return True
    return False

def can_win(brd, player):
    for tup in winners:
        if all(brd[ix] == player for ix in tup):
            return True
    return False

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move] = player
        win = can_win(brd, player)
        if undo:
            brd[move] = move
        return (True, win)
    return (False, False)

def computer_move():
    move = -1
    # Check if computer can win
    for i in range(9):
        if make_move(board, computer, i, True)[1]:
            move = i
            break
    
    # Check if player can win (block)
    if move == -1:
        for i in range(9):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    
    # Take preferred position
    if move == -1:
        for tup in moves:
            for mv in tup:
                if can_move(board, computer, mv):
                    move = mv
                    break
            if move != -1:
                break
    
    # If no strategic move, take any available
    if move == -1:
        available = [i for i in range(9) if can_move(board, computer, i)]
        if available:
            move = random.choice(available)
    
    return make_move(board, computer, move)

def space_exist():
    return any(isinstance(x, int) for x in board)

# Main game loop
player, computer = select_char()
print(f'Player is [{player}] and computer is [{computer}]')
result = '%%% Deuce ! %%%'

while space_exist():
    print_board()
    try:
        move = int(input('#Make your move ! [1-9] : ')) - 1
        if not (0 <= move < 9):
            raise ValueError
        moved, won = make_move(board, player, move)
        if not moved:
            print(' >> Invalid move! Try again!')
            continue
        
        if won:
            result = '*** Congratulations! You won! ***'
            break
        
        if space_exist():
            comp_moved, comp_won = computer_move()
            if comp_won:
                result = '=== You lose! ==='
                break
    except ValueError:
        print(' >> Invalid input! Enter a number 1-9!')
        continue

print_board()
print(result)