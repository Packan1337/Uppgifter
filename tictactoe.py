spot =["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Status check
Win = 1
Draw = -1
Stop = 1
Running = 0
Game = Running
Mark = "X"


# Function that prints game board
def draw_board():
    print(f'''
       a        b        c
            |       |
    1   {spot[0]}   |   {spot[1]}   |    {spot[2]}
            |       |
     -------|-------|--------
            |       |
    2   {spot[3]}   |   {spot[4]}   |    {spot[5]}
            |       |
     -------|-------|--------
            |       |
    3   {spot[6]}   |   {spot[7]}   |    {spot[8]}
            |       |        
    ''')


# Function to check for spot availability
def available_spot(x):
    if spot[x] == '-':
        return True
    else:
        return False


def status_check():
    global Game

    # Checking for horizontal win
    if spot[0] == spot[1] and spot[1] == spot[2] and spot[0] != "-":
        Game = Win
    elif spot[3] == spot[4] and spot[4] == spot[5] and spot[3] != "-":
        Game = Win
    elif spot[6] == spot[7] and spot[7] == spot[8] and spot[6] != "-":
        Game = Win

    # Checking for vertical win
    if spot[0] == spot[3] and spot[3] == spot[6] and spot[0] != "-":
        Game = Win
    elif spot[1] == spot[4] and spot[4] == spot[7] and spot[1] != "-":
        Game = Win
    elif spot[2] == spot[5] and spot[5] == spot[8] and spot[2] != "-":
        Game = Win

    # Checking for vertical win
    if spot[0] == spot[4] and spot[4] == spot[8] and spot[4] != "-":
        Game = Win
    elif spot[2] == spot[4] and spot[4] == spot[6] and spot[4] != "-":
        Game = Win
    elif spot[0] != "-"\
            and spot[1] != "-"\
            and spot[2] != "-"\
            and spot[3] != "-"\
            and spot[4] != "-"\
            and spot[5] != "-"\
            and spot[6] != "-"\
            and spot[7] != "-"\
            and spot[8] != "-":
        Game = Draw


print("Welcome to Packan's TicTacToe!")
print("(code partly stolen from the internet...)\n")
player = input("Enter name: ")
AI = "AI"