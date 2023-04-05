#Write a script to create a list with 5 string and count total number of string with even number of length with string using udf
def evenstrcount(a):
    v=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            v.append(i)
            count=count+1
    if(count>0):
        print(f'Even string number is {count} and string :{v}')
    else:
        print("Even string  not available.")

a=[]
for i in range(5):
    v1=input(f"Enter string:{i+1}:")
    a.append(v1)    
evenstrcount(a)    
