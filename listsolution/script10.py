#list10

def numcheak(lst):
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            return lst[i]
    return None

lst = [4, 5, 5, 5, 3, 8]

result = numcheck(lst)
if result:
    print("Output:", result)
else:
    print("List does not contain three consecutive common numbers."0)