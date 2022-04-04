from itertools import count
from bs4 import BeautifulSoup
import json
import requests
from task05 import movie_list

def analyse_language_director(movie_director_language):
    director_d={}
    for movie in movie_director_language:
        director_d[movie["Director"]]={}
    # print(director_d)
    for i in range(len(movie_director_language)):
        count=0
        for director in director_d:
            if director ==movie_director_language[i]["Director"]:
                language=movie_director_language[i]["Original Language"]
                count+=1
                director_d[director].update({language:count})
    
    file=open("task10.json","w")
    json.dump(director_d,file,indent=4)
    
    return director_d
        
    
analyse_language_director(movie_list)