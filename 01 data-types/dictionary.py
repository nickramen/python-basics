# Dictionary: is a data type that allows you to store and retrieve key-value pairs. They use commas for separation.
# Dictionaries are similar to lists and tuples in that they can hold multiple values, but unlike lists and tuples, 
# which use numeric indices to access elements, dictionaries use keys.

dictionary = {
    'name' : 'Nicole',
    'lastname' : 'Ramos',
    'age' : 22
}

print(type(dictionary))

print(dictionary)

# Access to an item in dictionary and modify it.
print(dictionary['name'])
print(dictionary['age'])

# Adding items to the dictionary. Look at the following two ways you can do it:
dictionary['nationality'] = "honduran"
dictionary.update({'student':False, 'profession':'programmer'})
print(dictionary)

# Updating items like the following:
dictionary['age'] = 25
dictionary.update({'student':True,'name':'Darcy'})
print(dictionary)