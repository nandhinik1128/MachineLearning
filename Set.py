'''Set is used to store multiple idems in a single variable.
UNORDERED UNCHANGEABLE . ONCE THE SET IS CREARED U CNANNOT CHANGE ITEMS
 BUT YOU CAN REMOVE ITEMS AND ADD NEW ITEMS,
 DUPLIACTES ARE NOT ALLOWED'''
'''Does not support indexing'''
#IN SET 1 AND TRUE IS CONSIDERED THE SAME
#IN SET 0 AND FALSE ARE CONSIDERED THE SAME
#WE CAN GET THE LENGTH OF THE SET THROUGHT THE FUNCTION "LEN"
set_1={0,1,3,2,0,3,4,1}#{0, 1, 2, 3, 4}
print(set_1)
'''here it removes the duplicate as set should not have
the duplicate values'''
set_2={"c","b","a","b","a"}#{'a', 'c', 'b'}
print(set_2)


#Inbuilt functions

#ADD
set_3={1,2,3}
print(set_3.add(4))#None insteaqd we should do the operation first and then print it

set_3.add(4)
print(set_3)

#DIFFERENCE
set_1={1,1,2,3,4}
set_2={1,2,3}
set_2.difference(set_1)
print(set_1)

#using constructor
thisset = set(("apple", "banana", "cherry")) 
# note the double round-brackets
