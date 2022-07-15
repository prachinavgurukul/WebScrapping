import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
a=soup.find('tbody',class_='lister-list')
b=a.find_all('tr')
c=[]
for i in b:
    movie_detail={}
    movie_name=i.find('td',class_="titleColumn").a.get_text()
    print(movie_name)
    movie_detail["movie_name"]=movie_name
    movie_rank=i.find('td',class_="titleColumn").get_text().strip()
    print(movie_rank[:3])
    movie_detail["movie_rank"]=movie_rank
    year_of_release=i.find('td',class_="titleColumn").span.get_text()
    print(year_of_release[1:5])
    movie_detail["year_of_release"]=year_of_release
    movie_link=i.find('td',class_="titleColumn").a['href']
    link='https://www.imdb.com'+movie_link
    print(link)
    movie_detail["link"]=link
    rating=i.find('td', class_="ratingColumn imdbRating").strong.get_text()
    print(rating)
    movie_detail["rating"]=rating
    c.append(movie_detail)
    pprint(c)
file=open('Movies_Detail.json','w')
json.dump(c,file,indent=4)




