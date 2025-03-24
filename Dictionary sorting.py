# Sample dictionary
my_dict = {
    'XX': 5,
    'BY': 10,
    'YY': 8,
    'AY': 2
}

# Sort via ascending - # for unuse
# sorted_items = sorted(my_dict.items(), key=lambda x: x[1])

#Sort via alphabetical
sorted_items = sorted(my_dict.items(), key=lambda x: x[0])

# Back to Dictionary
sorted_dict = dict(sorted_items)

# Print
print(sorted_dict)