import requests
from bs4 import BeautifulSoup
from csv import writer

baseurl = "https://github.com"
url = "https://github.com/topics/python"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("div",{"class":"col-md-8 col-lg-9"}).find_all("article")
count = 1

# print in terminal
for i in list:
    title = i.find("h3",{"class":"f3 color-fg-muted text-normal lh-condensed"}).find("a",{"class":"text-bold wb-break-word"}).text.strip()
    description = i.find("div",{"class":"px-3 pt-3"}).find("div").text.strip()
    link = i.find("h3",{"class":"f3 color-fg-muted text-normal lh-condensed"}).find("a",{"class":"text-bold wb-break-word"}).get("href")
    star = i.find("div",{"class":"d-flex flex-items-center"}).find("span",{"id":"repo-stars-counter-star"}).text.strip()
    last_update = i.find("ul",{"class":"d-flex f6 list-style-none color-fg-muted"}).find("relative-time",{"class":"no-wrap"}).text.strip()

    print(
        f"{count}\ntitle : {title}\ndescription : {description}\nlink : {baseurl+link}\nstar : {star}\nlast update: {last_update}\n--------------------"
    )

    count += 1



# writing to csv file
with open("topics.csv","w",encoding="UTF-8",newline="") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Title","Description","Link","Star","Last Update"])

    
    for i in list:
        title = i.find("h3",{"class":"f3 color-fg-muted text-normal lh-condensed"}).find("a",{"class":"text-bold wb-break-word"}).text.strip()
        description = i.find("div",{"class":"px-3 pt-3"}).find("div").text.strip()
        link = i.find("h3",{"class":"f3 color-fg-muted text-normal lh-condensed"}).find("a",{"class":"text-bold wb-break-word"}).get("href")
        star = i.find("div",{"class":"d-flex flex-items-center"}).find("span",{"id":"repo-stars-counter-star"}).text.strip()
        last_update = i.find("ul",{"class":"d-flex f6 list-style-none color-fg-muted"}).find("relative-time",{"class":"no-wrap"}).text.strip()


        csv_writer.writerow([title,description,baseurl+link,star,last_update])



