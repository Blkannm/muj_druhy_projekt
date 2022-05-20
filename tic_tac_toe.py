
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Trung Le
email: trung.le3301@gmail.com
discord: BLKANNM#1363
"""

from random import randrange

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

def win_condition():
    pass

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
        for radek in board:
            print(" | ".join(radek))
        
        if board_is_full(board):
            print("remiza")
            break
        #input hracu
        rada = int(input("vyber si radek: "))
        sloupec = int(input("vyber si sloupec: "))
        if (rada < 4 and rada > 0) and (sloupec < 4 and sloupec > 0):
            #koukne se pokud je pole volne
            if is_free_space(board[rada-1][sloupec-1]) == False:
                print("space is occupied")
                continue

            board[rada-1][sloupec-1] = player
            #vymeni na 2. hrace
            player = change_of_player(player)
        else:
            print("out of range!!")

            
    

tic_tac_toe()

