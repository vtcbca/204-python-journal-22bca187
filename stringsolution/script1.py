#python script to check string is palindrome or not
x=input("Enter any String :")
y=x[::-1]
if(x==y):
    print("String is Palindrome.")
else:
    print("String is Not Palindrome.")