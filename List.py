'''List is a data structure in python. it is mutable
and changeable.only the strings are should be enclosed within 
double quotes and it list is enclosed within [] and each element in the list is the 
item   '''
lst=["Mathematics",1,2,3,"Science"]
print(lst.append("Nandhini"))#adding atlast
print(lst)
print(lst.extend([5,6,7]))#adding more values at the end
print(lst)
print(lst[1])#"Indexing" gives the value tht is in tht index value
print(lst)
print(lst.insert(3,"Added new element in the particular location"))#can add the value at the specific location
print(lst)
print(lst[1:4])#slicing 4=n-1 and 1 is index value
print(lst)
lst1=[1,2,3,4]
print(sum(lst1))#summation of list elements
print(len(lst1))#length of the given list
print(lst1.index(2,0,3))
'''here 1 is the value we want to search and then 
0 and 3 are the index value and which returns the index value of the 
element tht i search for
'''
print(min(lst1))#minimum value in the list
print(lst1*5)#lst1 itself prints 5 times

