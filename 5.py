l1=[1,2,3,4]
l2=[1,2,3,4]
l3=[1,2,3,4]
l=list(map(lambda a,b,c:a+b+c,l1,l2,l3))
print(l)

fruits=['mango','orange','apple','banana']
z=list(filter(lambda x:'g' not in x ,fruits))
print(z)
