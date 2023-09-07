print("\n")
print("Welcome to Kaun Banega IAS")
print("\n")
name=input("Enter Your Name: ")
qreached=0
fflimit=3 #lifeline left
testended=1
#RESULTS
def result():
    if qreached == 0:
            percentage=100
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 1:
            percentage=99
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 2:
            percentage=92
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 3:
            percentage=86
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 4:
            percentage=72
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 5:
            percentage=66
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 6:
            percentage=47
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 7:
            percentage=31
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 8:
            percentage=20
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 9:
            percentage=8
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 10:
            percentage=0
            print("\nCongratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nKeep It Up!")
print("\n")

data=("Q1. Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?","A. Solicitor General","B. Attorney General", "C. Cabinet Secretary","D. Cheif Justice","Q2. Who, in 1978, became the first person to be born in the continent of Antarctica?","A. Emilio Palma","B. James Weddell","C. Amilio Gander", "D. Charles Wilkes","Q3. Which colonial power ended its involvement in India by selling the rights of the Nicobar islands to the British on October 18, 1868?","A. Belgium","B. Denmark","C. Italy","D. France","Q4. Who is the first women to successfully climb K2, the world's second highest mountain peak?","A. Junko Tabei","B. Wanda Rutkiewicz","C. Tamae Wantanabe","D. Cantal Mauduit","Q5. Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the \'Dastan-e-Ghadar\', a personal account of the 1857 revolt?","A. Mir Taqi Mir","B. Mohammad Ibrahim Zauq","C. Zahir Dehlvi","D. Abdul- Qasim Ferdowsi","Q6. The Historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were at which place in Shimla?","A. Viceregal Lodge","B. Gorton Castle","C. Barnes Court","D. Cecil Hotel","Q7. Where in SIngapore did Netaji Subhash Chandara Bose make the first proclamation of an Ajad Hind government?","A. Cathay Cinema Hall","B. Fort Canning PArk","C. National University of Singapore","D. National Gallery of Singapore","Q8. Milinda-Panha is a dialogue between King Menander or Milinda and which buddhist monk?","A. Asanga","B. Nagasena","C. Mahadharmarakshita","D. Dharmarakshita","Q9. Which was the first mountain peak above 8,000 meters in height to be submitted by Human?","A. Annapurna","B. Lhotse","C. Kanchenjunga","D. Makalu","Last Question!! What is the title of the Thesis that Dr. B R Ambedkar submitted to the LOndon School of Economics for which he was awarded his doctorate in 1923?","A. The wants and means of India","B. The problem of the Rupee","C. National Dividend of India","D. The Law and Lawyers")

print("*Important Instructions*\nType in the Option A,B,C,D whichever you think is Correct.\nYou have only Three 50-50 Life Lines (One Life Line per Question.)\nEnter \"5050\" to use it.")
print("\n")
input("(press ENTER key to begin)")
print("\n")

#1
if testended!=0:
    print(data[0]);print(data[1]);print(data[2]);print(data[3]);print(data[4])
    print("\n")
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
            print("\n",fflimit," Life Lines Left...\n");print(data[2]);print(data[4]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans1=="A" or enteredans1=="C" or enteredans1=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")

#2
if testended!=0:
    print(data[5]);print(data[6]);print(data[7]);print(data[8]);print(data[9])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans2=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[6]);print(data[8]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans2=="B" or enteredans2=="C" or enteredans2=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")

#3
if testended!=0:
    print(data[10]);print(data[11]);print(data[12]);print(data[13]);print(data[14])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans3=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[11]);print(data[12]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans3=="A" or enteredans3=="C" or enteredans3=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    

#4
if testended!=0:
    print(data[15]);print(data[16]);print(data[17]);print(data[18]);print(data[19])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans4=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[17]);print(data[18]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans4=="A" or enteredans4=="C" or enteredans4=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#5
if testended!=0:
    print(data[20]);print(data[21]);print(data[22]);print(data[23]);print(data[24])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans5=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[23]);print(data[24]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans5=="A" or enteredans5=="B" or enteredans5=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#6
if testended!=0:
    print(data[25]);print(data[26]);print(data[27]);print(data[28]);print(data[29])
    print("\n")
    while True:
        if fflimit!=0:
            rawans6=input("Enter A/B/C/D or 5050: ")
        else:
            rawans6=input("Enter A/B/C/D: ")
        enteredans6=rawans6.capitalize()

        if(enteredans6=="B"):
            qreached=qreached+1
            print("CORRECT!")
            print("\n")
            break
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans6=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[27]);print(data[29]);print("\n")
            while True:
                rawans65050=input("Enter B/D: ")
                enteredans65050=rawans65050.capitalize()
                
                if(enteredans65050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans65050=="D"):
                    testended=0
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans6=="A" or enteredans6=="C" or enteredans6=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#7
if testended!=0:
    print(data[30]);print(data[31]);print(data[32]);print(data[33]);print(data[34])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans7=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[31]);print(data[32]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans7=="A" or enteredans7=="C" or enteredans7=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#8
if testended!=0:
    print(data[35]);print(data[36]);print(data[37]);print(data[38]);print(data[39])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans8=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[37]);print(data[38]);print("\n")
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
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans8=="A" or enteredans8=="C" or enteredans8=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#9
if testended!=0:
    print(data[40]);print(data[41]);print(data[42]);print(data[43]);print(data[44])
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
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans9=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[41]);print(data[44]);print("\n")
            while True:
                rawans95050=input("Enter B/D: ")
                enteredans95050=rawans95050.capitalize()
                
                if(enteredans95050=="A"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    break
                elif(enteredans95050=="D"):
                    testended=0
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans9=="B" or enteredans9=="C" or enteredans9=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
    
#10
if testended!=0:
    print(data[45]);print(data[46]);print(data[47]);print(data[48]);print(data[49])
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
            break
        elif(fflimit==0 and enteredans1=="5050"):
            print("You Have 0 Life Lines Left.")
        elif (fflimit!=0 and enteredans10=="5050"):
            fflimit=fflimit-1
            print("\n",fflimit," Life Lines Left...\n");print(data[47]);print(data[49]);print("\n")
            while True:
                rawans105050=input("Enter B/D: ")
                enteredans105050=rawans105050.capitalize()
                
                if(enteredans105050=="B"):
                    qreached=qreached+1
                    print("CORRECT!")
                    print("\n")
                    print(result())
                    break
                elif(enteredans105050=="D"):
                    testended=0
                    print(result())
                    break
                else:
                    print("\nPlease Enter a Valid Input.")
                    
            break
        elif(enteredans10=="A" or enteredans10=="C" or enteredans10=="D"):
            testended=0
            print(result())
            break
        else:
            print("\nPlease Enter a Valid Input.")
