import requests
import json
import time
topic=input("Enter a topic: ")
current_year = time.strftime("%Y",time.localtime())
current_month = time.strftime("%m",time.localtime())
current_date = time.strftime("%d",time.localtime())
yest_int_date = int(current_date)-2
if yest_int_date<10:
    yest_int_date=f"0{yest_int_date}"


# Error Handeling
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
        print("Today's News will be available tomorrow",end="\n\n")

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