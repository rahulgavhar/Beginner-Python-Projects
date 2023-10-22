#My Personal Schedule
#5:30 wake up
#23:30 sleep

print("Make sure the python interpreter runs in your Time Zone.\n\n")
import time
tth=int(time.strftime('%H'))
ttm=int(time.strftime('%M'))

if (tth==5 and ttm>=30) or (tth>5 and tth<12):
    print("GOOD MORNING!")
    print("GOOD MORNING!")
    print("GOOD MORNING!")
elif (tth>=12 and tth<17):
    print("GOOD AFTERNOON!")
    print("GOOD AFTERNOON!")
    print("GOOD AFTERNOON!")
elif (tth>=17 and tth<23) or (tth==23 and ttm<30):
    print("GOOD EVENING!")
    print("GOOD EVENING!")
    print("GOOD EVENING!")
else:
    print("YOU SHOULD BE SLEEPING!")
    print("YOU SHOULD BE SLEEPING!")
    print("YOU SHOULD BE SLEEPING!")
