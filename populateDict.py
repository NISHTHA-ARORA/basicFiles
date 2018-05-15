a=[] #empty list
dic = {}
for i in range(3):
    name=raw_input(" name")
    year=raw_input(" year")
    branch=raw_input(" branch")

    dic["name"]=name
    dic["year"]=year
    dic["branch"]=branch
    print dic
    a.append(dic)

print a
