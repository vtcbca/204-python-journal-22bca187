def evenstring(a):
    v=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            v.append(i)
            count=count+1
    if(count>0):
        print(f'Even string is {count} and string :{v}')
    else:
        print( "even string is not available.")

a=[]
for i in range(5):
    v1=input(f"Enter string:{i+1}:")
    a.append(v1)    
evenstring(a)    