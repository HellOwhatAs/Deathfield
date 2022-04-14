a=[]
s,e=10,14
for i in range(s,e):
    with open("{}.jpg".format(i),"rb") as f:
        a.append(f.read())
for iii,i in enumerate(range(s,e)):
    with open("{}.jpg".format(i-1),"wb") as f:
        f.write(a[iii])