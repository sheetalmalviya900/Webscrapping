from bs4 import BeautifulSoup
import json
import requests

def scrap_top_list():

    url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    page=requests.get(url)

    soup=BeautifulSoup(page.text,"html.parser")

    main_div=soup.find('div', class_='panel-body content_body allow-overflow')
    table=soup.find("table",class_="table")
    trs=table.find_all('tr')
    
    movie_rank=[]
    movie_name=[]
    movie_rating=[]
    movie_year=[]
    movie_url=[]

    # print(trs)

    for tr in trs[1:]: 
        # print(trs)
        position=tr.find('td', class_="bold").get_text()
        rank=""
        # print(position)
    
        for i in position:
            if "." not in i:
                rank=rank+i
            else:
                break 
        movie_rank.append(rank)

        title=tr.find('a' , class_="unstyled articleLink").get_text().split()
        name=""
        for i in title[:-1]:
            name+=i
            # print(name)
        movie_name.append(name)
        year=title[-1][1:5]
        movie_year.append(year)
        url=tr.find('a' , class_="unstyled articleLink")
        link=url['href']
        link1="https://www.rottentomatoes.com/"+link
        movie_url.append(link1)

        imdbeating=tr.find('span' , class_="tMeterScore").get_text().strip()
        movie_rating.append(imdbeating)

    top_movie=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_rank)):
        details["position"]=int(movie_rank[i])
        details["name"]=str(movie_name[i])
        details["year"]=str(movie_year[i])
        details["rating"]=str(movie_rating[i])
        details["url"]=str(movie_url[i])
        top_movie.append(details.copy())


    with open("task01.json","w") as file:
        json.dump(top_movie,file,indent=4)

    return top_movie

task_2=scrap_top_list()