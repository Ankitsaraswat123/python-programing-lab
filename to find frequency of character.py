#to find the frequency of character in a string
a='ankit'
d={}
for i in len(a):
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print('frequency of ginem=n string is :\n',d)
