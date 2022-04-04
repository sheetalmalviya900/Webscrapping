from task02 import dec
import json

def group_by_decades(movie):
    list1=[]
    moviedec={}
    for i in movie:
        mode=int(i)%10
        decades=int(i)-mode
        if decades not in list1:
            list1.append(decades)
    list1.sort()
    for i in list1:
        moviedec[i]=[]

    for i in moviedec:
        dec10=i+9
        for x in movie:
            x=int(x)
            if x<=dec10 and x>=i:
                x=str(x)
                for v in movie[x]:
                    moviedec[i].append(v)
    
    file=open("task03.json","w")
    json.dump(moviedec,file,indent=4)

    return moviedec
group_by_decades(dec)