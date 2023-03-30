myDict = {
    "Fast": "In a Quick Manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'harry': 'Player'}
}

print(myDict['Fast'])
print(myDict['Harry'])
print(myDict)
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])