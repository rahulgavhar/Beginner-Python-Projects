# News API
import requests
import json
import time
print(f"News from {current_date}-{current_month}-{current_year} till 2016 is Available...")
topic=input("Enter a topic: ")
current_year = time.strftime("%Y",time.localtime())
current_month = time.strftime("%m",time.localtime())
current_date = time.strftime("%d",time.localtime())
# Error Handeling
while True:
    try:
        date=input(f"Enter any date between ({current_month}2016-{current_month}{current_year[2:4]}) YYYY-MM-DD format: ")
        if len(date)==10:
            if (int(date[0:4])>2015) and (int(date[0:4])<=int(current_year)):
                if int(date[0:4])==int(current_year) and (int(date[5:7])>0 and int(date[5:7])<=int(current_month)):
                    if (int(date[5:7])==int(current_month)) and (int(date[8:10])>0 and int(date[8:10])<int(current_date)):
                        break
                    elif (int(date[5:7])==int(current_month)) and (int(date[8:10])>0 and int(date[8:10])==int(current_date)):
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
        print("Enter the date in YYYY-MM-DD format",end="\n\n")
    except IndexError:
        print("Invalid Date",end="\n\n")
        time.sleep(1)
    except NameError:
        print("Today's News will be available tomorrow",end="\n\n)
              
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
