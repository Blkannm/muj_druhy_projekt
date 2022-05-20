
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Trung Le
email: trung.le3301@gmail.com
discord: BLKANNM#1363
"""


def board_is_full(board):
    for row in board:
        for item in row:
            if item == "-":
                return False
    return True

def is_free_space(space:str) -> bool:
    if space == "-":
        return True
    else:
        return False

def win_condition(current_board:list,player:str) -> bool:
    win = None
    # kontrola radku
    for i in range(3):
        win = True
        for j in range(3):
            if current_board[i][j] != player:
                win = False
        if win:
            return True
    # kontrola sloupcu
    for i in range(3):
        win = True
        for j in range(3):
            if current_board[j][i] != player:
                win = False
        if win:
            return True
    # kontrola Krizku
    win = True
    for i in range(3):
        if current_board[i][i] != player:
            win = False
    if win:
        return True
    win = True
    for i in range(3):
        if current_board[i][2 - i] != player:
            win = False
            break
    if win:
        return win



    else:
        return False
    
    

def change_of_player(hrac:str) -> str:
    if hrac == "X":
        return "O"
    if hrac == "O":
        return "X"

rozdelovac = "="*30
board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]
    
def tic_tac_toe():

    print("Welcome to Tic Tac Toe")
    print(rozdelovac)
    print(
        """
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row
    """
    )
    print(rozdelovac)
    print("Let's start the game")
    print(rozdelovac)
    player = "X"
    while True:
        #vypis herni desky
        for radek in board:
            print(" | ".join(radek))
        
    
        if board_is_full(board):
            print("remiza")
            break
        print( "-"*40 ,f"Hrac '{player}' | Zadej cisla od 1 do 3:    ", "-"*40, sep="\n")

        #input hracu
        input1 = input("vyber si radek: ")
        input2 = input("vyber si sloupec: ")
        if (input1.isnumeric() == False) or (input2.isnumeric() == False):
            print("zadej cisla od 1 do 3.")
            continue 
        rada = int(input1)
        sloupec = int(input2)
        if (rada < 4 and rada > 0) and (sloupec < 4 and sloupec > 0):
            #koukne se pokud je pole volne
            if is_free_space(board[rada-1][sloupec-1]) == False:
                print("mysto je zabrane!")
                continue

            board[rada-1][sloupec-1] = player
        else:
            print("mimo dosah")
            continue

        #win kondice
        if win_condition(board, player):
            for radek in board:
                print(" | ".join(radek))
            print(f"Hrac '{player}' vyhral!")
            break


        #vymeni na 1./2. hrace
        player = change_of_player(player)
            
    

if __name__ == "__main__":
    print("Nahrávání modulu..")
    tic_tac_toe()


