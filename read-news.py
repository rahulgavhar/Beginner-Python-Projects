import requests
import json
import time
import pycountry

api_key = "b0d19ed15a354c288823a2846cfb3d2a"
print("Welcome to News Reader")
print(f"How would you like to Read?\n1. Today's Headlines\n2. Specific Topic\n")

while True:
    try:
        choice=input("Enter your choice(1/2): ")
        if choice=="1" or choice=="2":
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
        
if choice=="2":
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
