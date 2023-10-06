import requests
import json
import time

print("How would you like to Read?\n1. Top Headlines\n2. For Specific Date\n(1-Top Headlines 2-Specific Date)\n")
while True:
    try:
        choice=input("Enter your choice(1/2): ")
        if choice=="1" or choice=="2":
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid Choice\n")
        time.sleep(1)

# Error Handeling for Top Headlines
if choice=="1":
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b0d19ed15a354c288823a2846cfb3d2a"

    response = requests.get(url)
    news = json.loads(response.text)

    for article in news["articles"]:
        print("----------------------------------")
        print("Article:")
        print(article["title"])
        print()
        print("Description:")
        print(article["description"])
        print("More info:",end=" ")
        print(article["url"])


# Error Handeling For Specific Date
topic=input("Enter a topic: ")
current_year = time.strftime("%Y",time.localtime())
current_month = time.strftime("%m",time.localtime())
current_date = time.strftime("%d",time.localtime())
yest_int_date = int(current_date)-2
if choice=="2":
    if yest_int_date<10:
        yest_int_date=f"0{yest_int_date}"
    while True:
        try:
            date=input(f"Enter any date between ({yest_int_date}-{current_month}-{current_year} till 2016) in DD-MM-YYYY format: ")
            if len(date)==10:
                if (int(date[6:10])>2015) and (int(date[6:10])<=int(current_year)):
                    if int(date[6:10])==int(current_year):
                        if (int(date[3:5])>0 and int(date[3:5])<=int(current_month)):
                            if (int(date[3:5])==int(current_month)) and (int(date[0:2])>0 and int(date[0:2])<int(current_date)):
                                break
                            elif (int(date[3:5])==int(current_month)) and (int(date[0:2])>0 and int(date[0:2])==int(current_date)):
                                raise NameError
                            elif (int(date[3:5])==int(current_month)) and (int(date[0:2])>0 and int(date[0:2])<int(current_date)):
                                raise IndexError
                            else:
                                raise IndexError
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
            print("Enter the date in DD-MM-YYYY format",end="\n\n")
        except IndexError:
            print("Invalid Date",end="\n\n")
            time.sleep(1)
        except NameError:
            print("Today's News will be available Soon...",end="\n\n")

    #converts date to YYYY-MM-DD format
    date=date[6:10]+"-"+date[3:5]+"-"+date[0:2]

    url = f"https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=popularity&apiKey=b0d19ed15a354c288823a2846cfb3d2a"

    response = requests.get(url)
    news = json.loads(response.text)

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