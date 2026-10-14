'''Tuples are something which stores the multiple items 
in a single variable.Ordered and unchangeable'''
#Tuples can be written with parantheses
'''Cannot change a single item but can can replace the whole tuple'''
t=(1,2,3)
print(t)
#it can be created without parantheses
t=1,2,3
print(t)
print(type(t))
print(t[0])
print(len(t))


#Constuctor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)