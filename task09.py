from bs4 import BeautifulSoup
import json
import os,random,time
import requests
from task01 import task_2
from task04 import scrap_movie_detail

for i in range(11):
    url=task_2[i]["url"]
    # print(url)
    def movie_detail(movie_url):
        random_sleep=random.randint(1,3)
        movie_name=""
        for i in movie_url[34:]:
            movie_name+=i
        # print(movie_name)
        file_name="task09"+movie_name+".json"
        text=os.path.exists(file_name)
        if text==True:
            file=open(file_name,"r")
            a=json.load(file)

        else:
            time.sleep(random_sleep)
            data=scrap_movie_detail(movie_url)
            file=open(file_name,"w")
            json.dump(data,file,indent=6)

    movie_detail(url)