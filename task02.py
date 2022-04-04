import json
from task01 import task_2

def group_by_year(movies):
    years=[]
    for i in movies:
        NUMBER=i["year"]
        if NUMBER not in years:
            years.append(NUMBER)
    
    movie_dict={}
    for i in years:
        movie_dict[i]=[]
        for j in movies:
            if i==j["year"]:
                movie_dict[i].append(j)
    return (movie_dict)
    file=open("task02.json","w")
    json.dump(movie_dict,file,indent=4)
    return (movie_dict)

dec=group_by_year(task_2)
