#list8
#Write a script to Replace list’s item with new value if found. Take value from user which you want to replace.

list1 = [5, 10, 15, 20, 25, 50, 20]
replace = int(input("Enter value you want to replace: "))
new_value = int(input("Enter value from which you want to replace: "))


for i in range(len(list1)):
    
    if list1[i] == replace:
  
        list1[i] = new_value

print(list1)