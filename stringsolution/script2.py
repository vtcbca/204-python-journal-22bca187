#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def paliwordcount(x):
    y=x.split(" ")
    z=0
    w=[]
    for i in y:
        if (i==i[::-1]):
            z=z+1
            w.append(i)
    if z>0:
        print(" Palindrome Word In Sentence Is {z} And Palindrome Words Are:{w}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
x=input("enter a sentece:")
paliwordcount(x)