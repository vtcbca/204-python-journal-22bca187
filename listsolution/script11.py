list11

#Write a Python program to enter sentence of atleast 10 words. Take user input of lengtho of word. 

inputstr= input("Enter a sentence of at least 10 words: ")


min_length = int(input("Enter the minimum word length: "))
words = inputstr.split()
result_dict = {}
for word in words:
    if len(word) >= min_length:
        result_dict[word] = len(word)


print(result_dict)