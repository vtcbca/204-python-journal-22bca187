list7

#Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.

names = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]

for i in range(len(names)):
    if names[i].endswith(".c"):
        names[i] = names[i].replace(".c", ".py")
print(names)