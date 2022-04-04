from turtle import title
from bs4 import BeautifulSoup
import json
import os
import requests
from task01 import task_2
from task04 import scrap_movie_detail

url=task_2[0]["url"]
# print(url)
def movie_detail(movie_url):
    movie_name=""
    for i in movie_url[34:]:
        movie_name+=i
    # print(movie_name)
    file_name="task08"+movie_name+".json"
    text=os.path.exists(file_name)
    if text==True:
        file=open(file_name,"r")
        a=json.load(file)
        

    else:
        data=scrap_movie_detail(movie_url)
        file=open(file_name,"w")
        json.dump(data,file,indent=6)
        return data
        

movie_detail(url)