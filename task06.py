from turtle import title
from bs4 import BeautifulSoup
import json
import requests
from task05 import movie_list

list=[]
def analyse_movies_language(movie_language):
    for i in movie_language:
        language=i["Original Language"]
        list.append(language)
    dict_language={}
    for i in list:
        count=0
        for j in list:
            if j==i:
                count+=1
        dict_language[i]=count

    file=open("task06.json","w")
    json.dump(dict_language,file,indent=4)

    return dict_language

analyse_movies_language(movie_list)