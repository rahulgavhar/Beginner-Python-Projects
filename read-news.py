import requests
import json
import time
import pycountry

api_key = "b0d19ed15a354c288823a2846cfb3d2a"

current_year = time.strftime("%Y",time.localtime())
current_month = time.strftime("%m",time.localtime())
current_date = time.strftime("%d",time.localtime())

yest_int_date = int(current_date)-2
if yest_int_date<10:
    yest_int_date=f"0{yest_int_date}"
previous_month = int(current_month)-1
if previous_month<10:
    previous_month=f"0{previous_month}"
    previous_year=current_year
    if previous_month==0:
        previous_month="12"
        previous_year=int(current_year)-1
tommorow_date = int(current_date)+1
if tommorow_date<10:
    tommorow_date=f"0{tommorow_date}"

if int(current_date)<=2:
    yest_int_date=30
    previous_month=int(current_month)-1
    if previous_month<10:
        previous_month=f"0{previous_month}"
        previous_year=current_year
        if previous_month==0:
            previous_month="12"
            previous_year=int(current_year)-1
    tommorow_date=int(current_date)+1
    if tommorow_date<10:
        tommorow_date=f"0{tommorow_date}"

#starts the program
print(f"How would you like to Read?\n1. Today's Headlines\n2. News from ({yest_int_date}-{current_month}-{current_year} to {tommorow_date}-{previous_month}-{previous_year})\n3. Specific Topic\n")
while True:
    try:
        choice=input("Enter your choice(1/2/3): ")
        if choice=="1" or choice=="2" or choice=="3":
            break
        else:
            raise Exception
    except Exception:
        print("Invalid Choice\n")
        time.sleep(1)

# Error Handeling for Top Headlines
if choice=="1":
    while True:
        try:
            country=input("Enter your Country Name: ")
            cc=pycountry.countries.search_fuzzy(country)[0].alpha_2
            break
        except Exception:
            print("Invalid Country Name")
            time.sleep(1)
        
    url = f"https://newsapi.org/v2/top-headlines?country={cc}&apiKey={api_key}"

    response = requests.get(url)
    news = json.loads(response.text)
    
    if news["articles"]!=[]:
        for article in news["articles"]:
            print("----------------------------------")
            print("Article:")
            print(article["title"])
            print()
            print("Description:")
            print(article["description"])
            print("More info:",end=" ")
            print(article["url"])
    else:
        print(f"No Articles Found for {country}")
        
# Error Handeling For Specific Date
if choice=="2":
    while True:
        try:
            date=input(f"Enter any date between ({yest_int_date}-{current_month}-{current_year} till {tommorow_date}-{previous_month}-{previous_year}) in DD-MM-YYYY format: ")
            if len(date)==10:
                if (int(date[6:10])==current_year or int(date[6:10]==previous_year)) and (int(date[3:5])>0 and int(date[3:5])<=12) and (int(date[0:2])>0 and int(date[0:2])<=31):
                        if (int(date[3:5])<int(current_month) or int(date[3:5]==int(previous_month))) and int(date[0:2])<=int(yest_int_date):
                            break
                        elif int(date[3:5])==int(current_month):
                            if (int(date[0:2])>0 and int(date[0:2])<int(current_date)-1):
                                break
                            else:
                                raise IndexError
                        else:
                            raise IndexError
                else:
                    raise IndexError
            else:
                raise ValueError
        except ValueError:
            print("Invalid Date")
            time.sleep(1)
            print("Enter the date in \"DD-MM-YYYY\" format Only.",end="\n\n")
        except IndexError:
            print("Invalid Date",end="\n\n")
            time.sleep(1)
        except NameError:
            print("Today's News will be available Soon...",end="\n\n")

    #converts date to YYYY-MM-DD format
    date=date[6:10]+"-"+date[3:5]+"-"+date[0:2]
    url = f"https://newsapi.org/v2/everything?q={date}&from={date}&sortBy=relevancy&apiKey={api_key}"

    response = requests.get(url)
    news = json.loads(response.text)

    if news["articles"]!=[]:
        for article in news["articles"]:
            print("----------------------------------")
            print("Article:")
            print(article["title"])
            print()
            print("Description:")
            print(article["description"])
            print()
            print("More info:",end=" ")
            print(article["url"])
    else:
        print(f"Cannot show news for {date}")
        
if choice=="3":
    topic=input("Enter the topic: ")
    url = f"https://newsapi.org/v2/everything?q={topic}&language=en&from=&sortBy=relevancy&pagesize=25&apiKey={api_key}"

    response = requests.get(url)
    news = json.loads(response.text)

    if news["articles"]!=[]:
        for article in news["articles"]:
            print("----------------------------------")
            print("Article:")
            print(article["title"])
            print()
            print("Description:")
            print(article["description"])
            print()
            print("More info:",end=" ")
            print(article["url"])
    else:
        print(f"No Articles Found for {topic}")
