"""
Maximum Key:

Find the key with the maximum value in a dictionary.
"""
save_money = {'Natanael': -100, 'Luis': 140, 'michael': 110}

max_key = max(zip(save_money.values(), save_money.keys()))[1]
print(max_key)

# other method 

# Initialize the dictionary
d = {'a': 10, 'b': 20, 'c': 60, 'd': 40, 'e': 50}

max_key = next(iter(d))
# print(max_key)

for key in d:
    if d[key] > d[max_key]:
        max_key = key
        
print(max_key)