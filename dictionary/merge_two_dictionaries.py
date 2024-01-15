"""
Merge Two Dictionaries:

Create two dictionaries and write a program 
to merge them into a single dictionary.
"""
def merge_dictionaries(dictionary_a, dictionary_b):
    
    for index in dictionary_b:
        if index not in dictionary_a:
            dictionary_a[index] = dictionary_b[index]
            
    return dictionary_a
    
def other_merge_dictionaries(dictionary_a, dictionary_b):
    return {**dictionary_a, **dictionary_b}

a = {"name": "Rudys", "last": "Acosta"}
b = {"name": "Natanael", "age": 36}

print(other_merge_dictionaries(a, b))