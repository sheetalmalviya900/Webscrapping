from turtle import title
from bs4 import BeautifulSoup
import json
import requests
from task01 import task_2

list=[]
for i in range(20):
    url=task_2[i]["url"]
    
    def scrap_movie_detail(movie_url):
        page=requests.get(movie_url)
        soup=BeautifulSoup(page.text,"html.parser")
        title_div1=soup.find('div',class_="thumbnail-scoreboard-wrap")
        # print(title_div)
        title_div=title_div1.find("h1",class_="scoreboard__title").get_text()

        poster=title_div1.find('img',class_="posterImage js-lazyLoad")
        poster1=poster["src"]

        s=soup.find('ul',class_="content-meta info")
            
        genre=s.find('div',class_="meta-value genre").get_text().split()
        # print(genre)

        sub_title=s.find_all("li",class_="meta-row clearfix")
        # print(sub_title)
        movie_d={}

        movie_d["Name"]=title_div
        for i in sub_title:
            k=i.find("div",class_="meta-label subtle").get_text()
            key=k[:-1]
            # print(key)
            value=i.find("div",class_="meta-value").get_text().strip().replace(" ","").replace("\n","").replace("\u00a0"," ")
            movie_d[key]=value
        # print(movie_d)
        time=int(movie_d["Runtime"][0])*60
        for i in movie_d['Runtime'][2:]:
            if 'm' not in i:
                time+=int(i)
            else:
                break
        movie_d["Runtime"]=str(time)+"Min."
        movie_d["Genre"]=genre
        movie_d["poster_url"]=poster1

        list.append(movie_d)

        file=open("task05.json","w")
        json.dump(list,file,indent=4)

        return list

    movie_list=scrap_movie_detail(url)

