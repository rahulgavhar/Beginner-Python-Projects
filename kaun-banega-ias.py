print("\n")
print("Welcome to Kaun Banega IAS")
print("\n")
name=input("Enter Your Name: ")
qreached=0
fflimit=3 #lifeline left
testended=1
#RESULTS
def result(name):
    if qreached == 0:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[2]}" + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"100"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 1:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[6]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"99"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 2:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[12]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"92"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 3:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[17]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"86"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 4:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[23]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"72"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 5:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[26]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"59"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 6:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[32]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"45"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 7:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[37]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"31"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 8:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[41]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"20"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 9:
            return "\n" + "Incorrect Answer." + f"\nCorrect Answer is {data[47]} " + "\n\n" +name+"\U0001F614\n"+"Your probability of Failing in UPSE is "+"8"+"%\nJara Padhai Likhai Karo. IAYAS Bano."
    elif qreached == 10:
            return "\n" + "Congratulations "+name+" \U0001F389\U0001F389"+"\nYou will easily pass UPSC. "+"\nKEEP IT UP!\U0001F44D"
print("\n")

data=("Q1. Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?","A. Solicitor General","B. Attorney General", "C. Cabinet Secretary","D. Cheif Justice","Q2. Who, in 1978, became the first person to be born in the continent of Antarctica?","A. Emilio Palma","B. James Weddell","C. Amilio Gander", "D. Charles Wilkes","Q3. Which colonial power ended its involvement in India by selling the rights of the Nicobar islands to the British on October 18, 1868?","A. Belgium","B. Denmark","C. Italy","D. France","Q4. Who is the first women to successfully climb K2, the world's second highest mountain peak?","A. Junko Tabei","B. Wanda Rutkiewicz","C. Tamae Wantanabe","D. Cantal Mauduit","Q5. Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the \'Dastan-e-Ghadar\', a personal account of the 1857 revolt?","A. Mir Taqi Mir","B. Mohammad Ibrahim Zauq","C. Zahir Dehlvi","D. Abdul- Qasim Ferdowsi","Q6. The Historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were at which place in Shimla?","A. Viceregal Lodge","B. Gorton Castle","C. Barnes Court","D. Cecil Hotel","Q7. Where in Singapore did Netaji Subhash Chandara Bose make the first proclamation of an Ajad Hind government?","A. Cathay Cinema Hall","B. Fort Canning PArk","C. National University of Singapore","D. National Gallery of Singapore","Q8. Milinda-Panha is a dialogue between King Menander or Milinda and which buddhist monk?","A. Asanga","B. Nagasena","C. Mahadharmarakshita","D. Dharmarakshita","Q9. Which was the first mountain peak above 8,000 meters in height to be submitted by Human?","A. Annapurna","B. Lhotse","C. Kanchenjunga","D. Makalu","Last Question!! \nWhat is the title of the Thesis that Dr. B R Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?","A. The wants and means of India","B. The problem of the Rupee","C. National Dividend of India","D. The Law and Lawyers")

print("*Important Instructions*\nType in the Option A,B,C,D whichever you think is Correct.\nYou have only Three 50-50 Life Lines (One Life Line per Question.)\nEnter \"5050\" to use it.\nYou lose, if you enter the Wrong Option.")
print("\n")
input("(press ENTER key to begin)")
print("\n")

import time as t

def invinp():
    message="**Invalid Input**"
    count=0
    while count<6:
        print(f"{message}",end="\r")
        if count==1:
                message="**Invalid Input**"
        elif count==3:
                message="**Invalid Input**"
        elif count==5:
                message="**Invalid Input**"
        else:
            message="                     "
        count+=1
        t.sleep(0.8)

#1
if testended!=0:
    for i in data[0]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[1]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[2]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[3]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[4]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    while True:
        if fflimit!=0:
            rawans1=input("Enter A/B/C/D or 5050: ")
        else:
            rawans1=input("Enter A/B/C/D: ")
        enteredans1=rawans1.capitalize()

        if(enteredans1=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif(fflimit!=0 and enteredans1=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[2]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[4]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans15050=input("Enter B/D: ")
                enteredans15050=rawans15050.capitalize()
                
                if(enteredans15050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans15050=="D"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans1=="A" or enteredans1=="C" or enteredans1=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())

#2
if testended!=0:
    for i in data[5]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[6]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[7]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[8]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[9]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans2=input("Enter A/B/C/D or 5050: ")
        else:
            rawans2=input("Enter A/B/C/D: ")
        enteredans2=rawans2.capitalize()

        if(enteredans2=="A"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans2=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans2=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[6]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[8]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans25050=input("Enter A/C: ")
                enteredans25050=rawans25050.capitalize()
                
                if(enteredans25050=="A"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans25050=="C"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans2=="B" or enteredans2=="C" or enteredans2=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())

#3
if testended!=0:
    for i in data[10]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[11]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[12]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[13]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[14]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans3=input("Enter A/B/C/D or 5050: ")
        else:
            rawans3=input("Enter A/B/C/D: ")
        enteredans3=rawans3.capitalize()

        if(enteredans3=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans3=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans3=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[11]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[12]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans35050=input("Enter A/B: ")
                enteredans35050=rawans35050.capitalize()
                
                if(enteredans35050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans35050=="A"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans3=="A" or enteredans3=="C" or enteredans3=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    

#4
if testended!=0:
    for i in data[15]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[16]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[17]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[18]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[19]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans4=input("Enter A/B/C/D or 5050: ")
        else:
            rawans4=input("Enter A/B/C/D: ")
        enteredans4=rawans4.capitalize()

        if(enteredans4=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans4=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans4=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[17]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[18]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans45050=input("Enter B/C: ")
                enteredans45050=rawans45050.capitalize()
                
                if(enteredans45050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans45050=="C"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans4=="A" or enteredans4=="C" or enteredans4=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#5
if testended!=0:
    for i in data[20]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[21]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[22]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[23]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[24]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans5=input("Enter A/B/C/D or 5050: ")
        else:
            rawans5=input("Enter A/B/C/D: ")
        enteredans5=rawans5.capitalize()

        if(enteredans5=="C"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans5=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans5=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[23]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[24]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans55050=input("Enter C/D: ")
                enteredans55050=rawans55050.capitalize()
                
                if(enteredans55050=="C"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans55050=="D"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans5=="A" or enteredans5=="B" or enteredans5=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#6
if testended!=0:
    for i in data[25]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[26]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[27]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[28]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[29]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans6=input("Enter A/B/C/D or 5050: ")
        else:
            rawans6=input("Enter A/B/C/D: ")
        enteredans6=rawans6.capitalize()

        if(enteredans6=="A"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans6=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans6=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[26]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[29]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans65050=input("Enter A/D: ")
                enteredans65050=rawans65050.capitalize()
                
                if(enteredans65050=="A"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans65050=="D"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans6=="A" or enteredans6=="C" or enteredans6=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#7
if testended!=0:
    for i in data[30]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[31]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[32]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[33]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[34]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans7=input("Enter A/B/C/D or 5050: ")
        else:
            rawans7=input("Enter A/B/C/D: ")
        enteredans7=rawans7.capitalize()

        if(enteredans7=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans7=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans7=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[31]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[32]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans75050=input("Enter A/B: ")
                enteredans75050=rawans75050.capitalize()
                
                if(enteredans75050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans75050=="A"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans7=="A" or enteredans7=="C" or enteredans7=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#8
if testended!=0:
    for i in data[35]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[36]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[37]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[38]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[39]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans8=input("Enter A/B/C/D or 5050: ")
        else:
            rawans8=input("Enter A/B/C/D: ")
        enteredans8=rawans8.capitalize()

        if(enteredans8=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans8=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans8=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[37]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[38]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans85050=input("Enter B/C: ")
                enteredans85050=rawans85050.capitalize()
                
                if(enteredans85050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans85050=="C"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans8=="A" or enteredans8=="C" or enteredans8=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#9
if testended!=0:
    for i in data[40]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[41]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[42]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[43]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[44]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans9=input("Enter A/B/C/D or 5050: ")
        else:
            rawans9=input("Enter A/B/C/D: ")
        enteredans9=rawans9.capitalize()

        if(enteredans9=="A"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans9=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans9=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[41]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[44]:
                print(i,end="")
                t.sleep(0.05)
            print("\n")
            while True:
                rawans95050=input("Enter A/D: ")
                enteredans95050=rawans95050.capitalize()
                
                if(enteredans95050=="A"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans95050=="D"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans9=="B" or enteredans9=="C" or enteredans9=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
    
#10
if testended!=0:
    for i in data[45]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[46]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[47]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[48]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    for i in data[49]:
        print(i,end="")
        t.sleep(0.05)
    print("",end="\n")
    print("\n")
    while True:
        if fflimit!=0:
            rawans10=input("Enter A/B/C/D or 5050: ")
        else:
            rawans10=input("Enter A/B/C/D: ")
        enteredans10=rawans10.capitalize()

        if(enteredans10=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            print(result(str(name)))
            break
        elif(fflimit==0 and enteredans10=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans10=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n")
            for i in data[47]:
                print(i,end="")
                t.sleep(0.05)
            for i in data[49]:
                print(i,end="")
                t.sleep(0.05)
            
            print("\n")
            while True:
                rawans105050=input("Enter B/D: ")
                enteredans105050=rawans105050.capitalize()
                
                if(enteredans105050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    print(result(str(name)))
                    break
                elif(enteredans105050=="D"):
                    testended=0
                    print(result(str(name)))
                    break
                else:
                    print("\n",invinp())
                    
            break
        elif(enteredans10=="A" or enteredans10=="C" or enteredans10=="D"):
            testended=0
            print(result(str(name)))
            break
        else:
            print("\n",invinp())
