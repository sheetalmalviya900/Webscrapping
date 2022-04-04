from bs4 import BeautifulSoup
import json
import requests
from task05 import movie_list

list=[]
def analyse_movies_director(movie_director):
    for i in movie_director:
        director=i["Director"]
        list.append(director)
    dict_director={}
    for i in list:
        count=0
        for j in list:
            if i==j:
                count+=1
        dict_director[i]=count
    
    file=open("task07.json","w")
    json.dump(dict_director,file,indent=4)
    return dict_director


analyse_movies_director(movie_list)