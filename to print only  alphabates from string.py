#to print only alphates in a given string
st=input('please enter a string')
x=''
for i in st:
    if (i>='a' and i<='z')or(i>='A' and i<='Z'):
     x+=i
    else:
        pass
print(x)
