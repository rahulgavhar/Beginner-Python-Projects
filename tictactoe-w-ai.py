# u cant win
from time import sleep
from random import randint

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
            print("X Won the match")
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
    
def final_move():
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
        case="random"
        for x in one_move_cases:
            if sum(listo[x[0]],listo[x[1]],None)==2:
                if listx[x[2]]!=1:
                    valuex=x[2]+1
                    case="done"
                    break
                continue
            else:
                continue
        
    if case=="random":
        valuex=valid[randint(0,len(valid)-1)]
        
while True:
    
    if turn == 1:
        sleep(1)
        print("\nComputer's Turn")
        sleep(2)
        #computer played first
        if entered == []:
            valuex=5
        #computer player computer
        elif xentered==[5] and (oentered==[1] or oentered==[3] or oentered==[7] or oentered==[9]):
            case="condition 1"
            if oentered==[1]:
                valuex=9
            elif oentered==[3]:
                valuex=7
            elif oentered==[7]:
                valuex=3
            elif oentered==[9]:
                valuex=1
        elif xentered==[5] and (oentered==[2] or oentered==[4] or oentered==[6] or oentered==[8]):
            case="condition 2"
            if oentered==[2]:
                valuex=randint(1,3)
            elif oentered==[4]:
                valuex=randint(1,7)
            elif oentered==[6]:
                valuex=randint(3,9)
            elif oentered==[8]:
                valuex=randint(7,9)
        #computer player computer player computer
        elif case=="condition 1":
            #win condition for computer
            if xentered==[5,9] and (oentered==[1,4] or oentered==[1,2] or oentered==[1,8] or oentered==[1,6]):
                if oentered==[1,4]:
                    valuex=7
                elif oentered==[1,2]:
                    valuex=3
                elif oentered==[1,8]:
                    valuex=3
                elif oentered==[1,6]:
                    valuex=7
            elif xentered==[5,7] and (oentered==[3,2] or oentered==[3,6] or oentered==[3,8] or oentered==[3,4]):
                if oentered==[3,2]:
                    valuex=1
                elif oentered==[3,6]:
                    valuex=9
                elif oentered==[3,8]:
                    valuex=1
                elif oentered==[3,4]:
                    valuex=9
            elif xentered==[5,3] and (oentered==[7,8] or oentered==[7,4] or oentered==[7,2] or oentered==[7,6]):
                if oentered==[7,8]:
                    valuex=9
                elif oentered==[7,4]:
                    valuex=1
                elif oentered==[7,6]:
                    valuex=1
                elif oentered==[7,2]:
                    valuex=9
            elif xentered==[5,1] and (oentered==[9,6] or oentered==[9,8] or oentered==[9,4] or oentered==[9,2]):
                if oentered==[9,6]:
                    valuex=3
                elif oentered==[9,8]:
                    valuex=7
                elif oentered==[9,4]:
                    valuex=3
                elif oentered==[9,2]:
                    valuex=7
            #draw condition
            elif xentered==[5,9] and (oentered==[1,7] or oentered==[1,3]):
                if oentered==[1,7]:
                    valuex=4
                elif oentered==[1,3]:
                    valuex=2
            elif xentered==[5,7] and (oentered==[3,1] or oentered==[3,9]):
                if oentered==[3,1]:
                    valuex=2
                elif oentered==[3,9]:
                    valuex=6
            elif xentered==[5,3] and (oentered==[7,1] or oentered==[7,9]):
                if oentered==[7,1]:
                    valuex=4
                elif oentered==[7,9]:
                    valuex=8
            elif xentered==[5,1] and (oentered==[9,7] or oentered==[9,3]):
                if oentered==[9,7]:
                    valuex=8
                elif oentered==[9,3]:
                    valuex=6
        elif case=="condition 2":
            if (oentered==[2,9] and xentered==[5,1] ):
                valuex=7
            elif (oentered==[2,7] and xentered==[5,3]):
                valuex=9
            elif (oentered==[4,3] and xentered==[5,7] ):
                valuex=9
            elif (oentered==[4,9] and xentered==[5,1]):
                valuex=3
            elif (oentered==[6,1] and xentered==[5,9]):
                valuex=7
            elif (oentered==[6,3] and xentered==[5,7]):
                valuex=1
            elif (oentered==[8,3] and xentered==[5,7]):
                valuex=1
            elif (oentered==[8,1] and xentered==[5,9]):
                valuex=3
            
            
        #player computer
        elif oentered == [5]:
            valuex=randint(1,3,7,9)
        elif oentered == [1] or oentered==[3] or oentered==[7] or oentered==[9]:
            valuex=5
        elif oentered == [2] or oentered==[4] or oentered==[6] or oentered==[8]:
            valuex=5
        
        #player computer player computer
        elif (oentered == [1,9] and xentered==[5]) or (oentered==[3,7] and xentered==[5]):
            valuex=2
        elif oentered==[1,9] and xentered==[5,2]:
            pass
        
        
        if valuex==None:
            final_move()
            
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
    valuex=None
