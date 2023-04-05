#Write a script to create a list with 5 string and count total number of string with even number of length with string using U

def countevenstr(a):
    c=[]
    count = 0
    for b in a:
            if (len(b) % 2 == 0):
                c.append(b)
                count=count +1
    if(count>0):
        print("Even string is {count}and string:{c}")
    else:
        print("Even string is not available")
a=[]
for b in range(5):
    x=input("Enter string:{i+1}:")
    a.append(x)
countevenstr(a)    
