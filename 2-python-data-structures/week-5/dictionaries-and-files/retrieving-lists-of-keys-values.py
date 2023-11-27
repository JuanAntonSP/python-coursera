dd = {"chuck": 1, "fred": 42, "jan": 100}

# convert to list
print(list(dd))  # ['chuck', 'fred', 'jan']


print(dd.values())  # dict_values([1, 42, 100])
print(list(dd.values()))  # [1, 42, 100]
print(dd.items())  # dict_items([('chuck', 1), ('fred', 42), ('jan', 100)]) <- tuples
