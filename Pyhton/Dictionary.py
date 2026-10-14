''' Dictionaries are something which will
 store the keys and values. this is changeable
 and then same duplicates aer not allowed'''

d={
    "Name":"Nandhini",
    "Department":"AI&DS",
    "Year":"2"
}
print(d["Name"])
#Also we could find the dictionary length
print(len(d))
print(type(d))
d["Name"]="Dhiya"
print(d["Name"])


#Nested dictionary
Name_1={"Nandhini":"AD247"}
Name_2={"Dhiya":"AD158"}
Name_3={"Selvakarshan":"CS396"}
students={"stud1":Name_1,"stud2":Name_2,"stud3":Name_3}
print(students)
#{'stud1': {'Nandhini': 'AD247'}, 'stud2': {'Dhiya': 'AD158'}, 'stud3': {'Selvakarshan': 'CS396'}}
print(students["stud1"])


