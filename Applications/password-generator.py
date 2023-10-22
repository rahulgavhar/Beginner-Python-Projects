import random 
import string
import re
def generate_password(length): 
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(length))
    if password.find("\\") != -1:
        password = password.replace("\\","[")
    if password.find("'") != -1:
        password = password.replace("'",">")
    if password.find('"') != -1:
        password = password.replace('"',"<")
    if password.find("%") != -1:
        password = password.replace("%","|")
    return password
print("Do you want to generate a password or search for a password? ")
while True:
    purpose=input("Enter 'g' or 's': ")
    if purpose == "g" or purpose == "s":
        break
    else:
        print()

if purpose == "g":
    while True:
        while True:
            try:
                list_desc=[]
                pass_desc_letters=[]
                kw=[]
                pass_desc = input("\nEnter keyword for the password (if more sep w/ commas): ")
                pass_desc=re.sub(' +', '', pass_desc)
                if pass_desc.find("\\") != -1 or pass_desc.find("'") != -1 or pass_desc.find('"') != -1 or pass_desc.find("%") != -1 or pass_desc.find(":") != -1:
                    print("{\\,\',\",%,:} are not accepted.")
                    continue
                
                if pass_desc.find(",") != -1:
                    pass_desc_letters = pass_desc.split(",")
                else:
                    pass_desc_letters.append(pass_desc)
                    
                while "" in pass_desc_letters:
                    pass_desc_letters.remove("")
                
                if pass_desc_letters == []:
                    raise Exception("0 keywords entered.")
                
                for ii in pass_desc_letters:
                    pass_desc_lower = ii.lower()
                    list_desc.append(pass_desc_lower)
                
                print("\nKeywords entered: ",pass_desc_letters)
                while True:
                    try:
                        password_length = int(input("\nEnter the length of the password(5-19): "))
                        if password_length<5 or password_length>19:
                            print("\nPlease enter a valid length (5-19 characters)")
                            continue
                        else:
                            break
                    except Exception:
                        print("Please enter numbers only.")
                break
            except Exception as e:
                print("Error Occured: ",e)
                
        if len(list_desc)>1:
            ss=", "
            keyw=ss.join(list_desc)
        else:
            keyw=list_desc[0]
        
        generated_password = generate_password(password_length)
        print("\nSaved As:",f"\'{keyw}" + " : " + generated_password + "\' (in Password Folder/passwords.txt)\n")
        
        with open('Password Folder/passwords.txt','a') as f:
            f.write(keyw + " : " + generated_password + "\n")
        
        again=input("Do you want to generate another password? (Enter 'y'/'n): ")
        if again=="y":
            continue
        else:
            break
        
elif purpose == "s":
    while True:
        try:
            pass_desc = input("\nEnter keywords to search (separate w/ commas): ")
            pass_desc=re.sub(' +', '', pass_desc)
            if pass_desc.find("\\") != -1 or pass_desc.find("'") != -1 or pass_desc.find('"') != -1 or pass_desc.find("%") != -1 or pass_desc.find(":") != -1:
                print("{\\,\',\",%,:} are not accepted.")
                continue
            pass_desc=pass_desc.lower()
            sc=pass_desc.split(",")
            for zz in sc:
                while zz.find(" ") != -1:
                    try:
                        kw=zz.split(" ")
                        sc.extend(kw)
                        sc.remove(zz)
                    except:
                        break
            
            while "" in sc:
                sc.remove("")
            if len(sc) == 0:
                print("Please enter atleast 1 keyword.")
                continue
            print("\nKeywords entered: ",sc)
            print("\nPasswords found: ")
            count=0
            with open('Password Folder/passwords.txt','r') as f:
                for line in f:
                    cropped_line=line.split(" : ")[0]
                    for i in sc:
                        if cropped_line.find(i) != -1:
                            count+=1
                            
                            print(line,end="")
                else:
                    if count==0:
                        print("PASSWORD NOT FOUND.")
            if count==0:
                again=input("Do you want to search again? (Enter 'y' to continue): ")
                if again=="y":
                    continue
                else:
                    break
            break
        except Exception as e:
            print("Error Occured: ",e)
