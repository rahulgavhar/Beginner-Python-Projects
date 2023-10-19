# u cant win
from time import sleep
from random import randint
import random as r

def sum(a, b, c):
    if a!=None and b!=None and c!=None:
        return a + b + c
    elif a!=None and b!=None:
        return a + b

def play(listx, listo):
    one = 'X' if listx[0]==1 else ('O' if listo[0]==1 else 1)
    two = 'X' if listx[1]==1 else ('O' if listo[1]==1 else 2)
    three = 'X' if listx[2]==1 else ('O' if listo[2]==1 else 3)
    four = 'X' if listx[3]==1 else ('O' if listo[3]==1 else 4)
    five = 'X' if listx[4]==1 else ('O' if listo[4]==1 else 5)
    six = 'X' if listx[5]==1 else ('O' if listo[5]==1 else 6)
    seven = 'X' if listx[6]==1 else ('O' if listo[6]==1 else 7)
    eight = 'X' if listx[7]==1 else ('O' if listo[7]==1 else 8)
    nine = 'X' if listx[8]==1 else ('O' if listo[8]==1 else 9)
    print()
    print(f"{one} | {two} | {three} ")
    print(f"--|---|---")
    print(f"{four} | {five} | {six} ")
    print(f"--|---|---")
    print(f"{seven} | {eight} | {nine} ")

def winstatus(listx, listo, valid):
    win_cases = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
    for win in win_cases:
        if(sum(listx[win[0]], listx[win[1]], listx[win[2]]) == 3):
            play(listx, listo)
            print("Computer Won the match")
            return 1
        if(sum(listo[win[0]], listo[win[1]], listo[win[2]]) == 3):
            play(listx, listo)
            print("O Won the match")
            return 0
        if valid==[]:
            play(listx, listo)
            print("Match Drawn")
            return 2
    return -1
xentered=[]
oentered=[]
entered=[]
total=[1,2,3,4,5,6,7,8,9]
listx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
listo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Welcome to TicTacToe Game (with AI)\n")
print("Do you want to play first")
while True:
    try:
        choice=input("(Enter 'yes'/'no' to continue): ")
        if choice=="yes":
            turn=0
        elif choice=="no":
            turn=1
        else:
            raise Exception
        break
    except Exception:
        print()
    
def next_move():
    global valuex, valid
    one_move_cases=([0,1,2],[1,2,0],[0,2,1],[3,4,5],[4,5,3],[3,5,4],[6,7,8],[7,8,6],[6,8,7],[0,3,6],[3,6,0],[0,6,3],[1,4,7],[4,7,1],[1,7,4],[2,5,8],[5,8,2],[2,8,5],[0,4,8],[4,8,0],[0,8,4],[2,4,6],[4,6,2],[2,6,4])
    case="win"
    if case=="win":
        case="draw"
        for x in one_move_cases:
            if sum(listx[x[0]],listx[x[1]],None)==2:
                if listo[x[2]]!=1:
                    valuex=x[2]+1
                    case="done"
                    break
                continue
            else:
                continue
        
    if case=="draw":
        case="center"
        for x in one_move_cases:
            if sum(listo[x[0]],listo[x[1]],None)==2:
                if listx[x[2]]!=1:
                    valuex=x[2]+1
                    case="done"
                    break
                continue
            else:
                continue
    if case=="center":
        case="corner"
        if (listx[4]!=1 and listo[4!=1]):
            valuex=5
            case="done"
    if case=="corner":
        case="random"
        corner_list=[]
        if (listx[0]!=1 and listo[0]!=1):
            corner_list.append(0)
            case="done"
        if (listx[2]!=1 and listo[2]!=1):
            corner_list.append(2)
            case="done"
        if (listx[6]!=1 and listo[6]!=1):
            corner_list.append(6)
            case="done"
        if (listx[8]!=1 and listo[8]!=1):
            corner_list.append(8)
            case="done"
        valuex=corner_list[randint(0,len(corner_list)-1)]+1
    if case=="random":
        valuex=valid[randint(0,len(valid)-1)]
        
while True:
    if turn == 1:
        sleep(1)
        print("\nComputer's Turn")
        sleep(2)
        #computer played first
        
        next_move()
            
        entered.append(valuex)
        xentered.append(valuex)
        listx[valuex-1] = 1
        
    else:
        if entered == []:
            play(listx, listo)
        while True:
            try:
                print("\nYour Turn")
                valueo = int(input("Please enter a value: "))
                if valueo in total:
                    if valueo in entered:
                        print("X/O is already entered in this position")
                    else:
                        break
                else:
                    raise Exception
            except Exception:
                print(f"Please enter value from {valid}")
        entered.append(valueo)
        oentered.append(valueo)
        listo[valueo-1] = 1
        
    valid=[x for x in total if x not in entered]
    cwin = winstatus(listx, listo, valid)
    if cwin != -1:
        break
    play(listx, listo)
    turn = 1 - turn
