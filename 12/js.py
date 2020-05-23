import json

numbers = [1, 3243, 3243, 2, 544, 4564, 11, 354, 77, 2, 54, 4345, 6, 0]

f = open('numbers.json', 'w')
json.dump(numbers, f)
f.close()
