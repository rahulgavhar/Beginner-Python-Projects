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
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 1:
            percentage=99
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 2:
            percentage=92
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 3:
            percentage=86
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 4:
            percentage=72
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 5:
            percentage=66
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 6:
            percentage=47
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 7:
            percentage=31
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 8:
            percentage=20
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 9:
            percentage=8
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nJara Padhai Likhai Karo. IAYAS Bano.")
    elif qreached == 10:
            percentage=0
            print("Congratulations ",name," !!","\nYour probability of Failing in UPSE is ",percentage,"%\nKeep It Up!")
print("\n")

data=("Q1. Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?","A. Solicitor General","B. Attorney General", "C. Cabinet Secretary","D. Cheif Justice","Q2. Who, in 1978, became the first person to be born in the continent of Antarctica?","A. Emilio Palma","B. James Weddell","C. Amilio Gander", "D. Charles Wilkes","Q3. Which colonial power ended its involvement in India by selling the rights of the Nicobar islands to the British on October 18, 1868?","A. Belgium","B. Denmark","C. Italy","D. France","Q4. Who is the first women to successfully climb K2, the world's second highest mountain peak?","A. Junko Tabei","B. Wanda Rutkiewicz","C. Tamae Wantanabe","D. Cantal Mauduit","Q5. Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the \'Dastan-e-Ghadar\', a personal account of the 1857 revolt?","A. Mir Taqi Mir","B. Mohammad Ibrahim Zauq","C. Zahir Dehlvi","D. Abdul- Qasim Ferdowsi","Q6. The Historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were at which place in Shimla?","A. Viceregal Lodge","B. Gorton Castle","C. Barnes Court","D. Cecil Hotel","Q7. Where in SIngapore did Netaji Subhash Chandara Bose make the first proclamation of an Ajad Hind government?","A. Cathay Cinema Hall","B. Fort Canning PArk","C. National University of Singapore","D. National Gallery of Singapore","Q8. Milinda-Panha is a dialogue between King Menander or Milinda and which buddhist monk?","A. Asanga","B. Nagasena","C. Mahadharmarakshita","D. Dharmarakshita","Q9. Which was the first mountain peak above 8,000 meters in height to be submitted by Human?","A. Annapurna","B. Lhotse","C. Kanchenjunga","D. Makalu","Last Question. What is the title of the Thesis that Dr. B R Ambedkar submitted to the LOndon School of Economics for which he was awarded his doctorate in 1923?","A. The wants and means of India","B. The problem of the Rupee","C. National Dividend of India","D. The Law and Lawyers")

print("*Important Instructions*\nType in the Option A,B,C,D whichever you think is Correct.\nYou have only Three 50-50 Life Lines (One Life Line per Question.)\nEnter \"5050\" to use it.")
print("\n")
input("(press any key to begin)")
print("\n")

#
if testended!=0:
    print(data[0]);print(data[1]);print(data[2]);print(data[3]);print(data[4])
    print("\n")
    if fflimit!=0:
        rawans1=input("Enter A/B/C/D or 5050: ")
    else:
        rawans1=input("Enter A/B/C/D: ")
    print("\n")
    enteredans1=rawans1.capitalize()

    if(enteredans1=="B"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans1=="5050"):
        fflimit=fflimit-1
        print(fflimit," Life Lines Left...\n");print(data[2]);print(data[4]);print("\n")
        rawans15050=input("Enter A/B/C/D: ")
        enteredans15050=rawans1.capitalize()
        if(enteredans15050=="B"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())

#
if testended!=0:
    print(data[5]);print(data[6]);print(data[7]);print(data[8]);print(data[9])
    print("\n")
    if fflimit!=0:
        rawans2=input("Enter A/B/C/D or 5050: ")
    else:
        rawans2=input("Enter A/B/C/D: ")
    print("\n")
    enteredans2=rawans2.capitalize()

    if(enteredans2=="A"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans2=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[6]);print(data[9]);print("\n")
        rawans25050=input("Enter A/B/C/D: ")
        enteredans25050=rawans2.capitalize()
        if(enteredans25050=="A"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    

#
if testended!=0:
    print(data[10]);print(data[11]);print(data[12]);print(data[13]);print(data[14])
    print("\n")
    if fflimit!=0:
        rawans3=input("Enter A/B/C/D or 5050: ")
    else:
        rawans3=input("Enter A/B/C/D: ")
    print("\n")
    enteredans3=rawans3.capitalize()

    if(enteredans3=="B"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans3=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[11]);print(data[12]);print("\n")
        rawans35050=input("Enter A/B/C/D: ")
        enteredans35050=rawans3.capitalize()
        if(enteredans35050=="B"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    

#
if testended!=0:
    print(data[15]);print(data[16]);print(data[17]);print(data[18]);print(data[19])
    print("\n")
    if fflimit!=0:
        rawans4=input("Enter A/B/C/D or 5050: ")
    else:
        rawans4=input("Enter A/B/C/D: ")
    print("\n")
    enteredans4=rawans4.capitalize()

    if(enteredans4=="B"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans4=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[17]);print(data[18]);print("\n")
        rawans45050=input("Enter A/B/C/D: ")
        enteredans45050=rawans4.capitalize()
        if(enteredans45050=="B"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[20]);print(data[21]);print(data[22]);print(data[23]);print(data[24])
    print("\n")
    if fflimit!=0:
        rawans5=input("Enter A/B/C/D or 5050: ")
    else:
        rawans5=input("Enter A/B/C/D: ")
    print("\n")
    enteredans5=rawans5.capitalize()

    if(enteredans5=="C"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans5=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[21]);print(data[23]);print("\n")
        rawans55050=input("Enter A/B/C/D: ")
        enteredans55050=rawans5.capitalize()
        if(enteredans55050=="C"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[25]);print(data[26]);print(data[27]);print(data[28]);print(data[29])
    print("\n")
    if fflimit!=0:
        rawans6=input("Enter A/B/C/D or 5050: ")
    else:
        rawans6=input("Enter A/B/C/D: ")
    print("\n")
    enteredans6=rawans6.capitalize()

    if(enteredans6=="C"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans6=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[26]);print(data[28]);print("\n")
        rawans65050=input("Enter A/B/C/D: ")
        enteredans65050=rawans6.capitalize()
        if(enteredans65050=="C"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[30]);print(data[31]);print(data[32]);print(data[33]);print(data[34])
    print("\n")
    if fflimit!=0:
        rawans7=input("Enter A/B/C/D or 5050: ")
    else:
        rawans7=input("Enter A/B/C/D: ")
    print("\n")
    enteredans7=rawans7.capitalize()

    if(enteredans7=="A"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans7=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[31]);print(data[32]);print("\n")
        rawans75050=input("Enter A/B/C/D: ")
        enteredans75050=rawans7.capitalize()
        if(enteredans75050=="A"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[35]);print(data[36]);print(data[37]);print(data[38]);print(data[39])
    print("\n")
    if fflimit!=0:
        rawans8=input("Enter A/B/C/D or 5050: ")
    else:
        rawans8=input("Enter A/B/C/D: ")
    print("\n")
    enteredans8=rawans8.capitalize()

    if(enteredans8=="B"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans4=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[37]);print(data[39]);print("\n")
        rawans85050=input("Enter A/B/C/D: ")
        enteredans85050=rawans8.capitalize()
        if(enteredans85050=="B"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[40]);print(data[41]);print(data[42]);print(data[43]);print(data[44])
    print("\n")
    if fflimit!=0:
        rawans9=input("Enter A/B/C/D or 5050: ")
    else:
        rawans9=input("Enter A/B/C/D: ")
    print("\n")
    enteredans9=rawans9.capitalize()

    if(enteredans9=="A"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans9=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[41]);print(data[42]);print("\n")
        rawans95050=input("Enter A/B/C/D: ")
        enteredans95050=rawans9.capitalize()
        if(enteredans95050=="A"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())
    
#
if testended!=0:
    print(data[45]);print(data[46]);print(data[47]);print(data[48]);print(data[49])
    print("\n")
    if fflimit!=0:
        rawans10=input("Enter A/B/C/D or 5050: ")
    else:
        rawans10=input("Enter A/B/C/D: ")
    print("\n")
    enteredans10=rawans10.capitalize()

    if(enteredans10=="B"):
        qreached=qreached+1

    elif (fflimit!=0 and enteredans10=="5050"):
        fflimit=fflimit-1
        print(fflimit,"Life Lines Left...\n");print(data[46]);print(data[47]);print("\n")
        rawans105050=input("Enter A/B/C/D: ")
        enteredans105050=rawans10.capitalize()
        if(enteredans105050=="B"):
            qreached=qreached+1
        else:
            testended=0
            print(result())
    else:
        testended=0
        print(result())