from random import randint
def sum(a, b, c ):
    return a + b + c

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
    print(f"{seven} | {eight} | {nine} ")
    print(f"--|---|---")
    print(f"{four} | {five} | {six} ")
    print(f"--|---|---")
    print(f"{one} | {two} | {three} ")

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
    if valid == []:
        play(listx, listo)
        print("Match Draw")
        return 2
    return -1

entered=[]
total=[1,2,3,4,5,6,7,8,9]
valid=[1,2,3,4,5,6,7,8,9]
listx = [0, 0, 0, 0, 0, 0, 0, 0, 0]
listo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = randint(0, 1)
print("Welcome to 2 Player TicTacToe Game")
while True:
    if entered == []:
        play(listx, listo)
    if turn == 1:
        while True:
            try:
                print("\nX's Chance")
                valuex = int(input("Please enter a value: "))
                if valuex in total:
                    if valuex in entered:
                        print("X/O is already entered in this position")
                    else:
                        break
                else:
                    raise Exception
            except Exception:
                print(f"Please enter value from {valid}")
        entered.append(valuex)
        listx[valuex-1] = 1
    else:
        while True:
            try:
                print("\nO's Chance")
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
        listo[valueo-1] = 1
    valid=[x for x in total if x not in entered]
    cwin = winstatus(listx, listo, valid)
    if cwin != -1:
        break
    play(listx, listo)
    turn = 1 - turn
