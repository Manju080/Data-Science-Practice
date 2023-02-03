def searc(l,elem):
    i=0
    sea_res=False
    while(i<len(l) and sea_res is False):
    
        if l[i]==elem:
    
            sea_res= True
        else:
            i +=1
    return sea_res

print(searc([112,24,32,45,41],24))    