"""
Word Frequency Counter

Write a program that takes a string as input and returns
a dictionary showing the frequency of each word.
"""
string  = input("Give me a string: ")
frequency = frequency_a = {}


string = string.strip()

# simple way
for i in string:
    if i not in frequency:
        frequency[i] = string.count(i)
        
        
# no use string method way        
for i in string:
    if i in frequency_a:
        frequency_a[i] += 1
    else:
        frequency_a[i] = 1       
    
print(frequency, frequency_a)