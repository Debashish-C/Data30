# A tuple in python is an ordered, immutable collection of elements.
#creating a tuple
mixed = (10,"hello",90.90,True)
print(mixed)

#empty tuple
empty = ()

#single element tuple very important
single = (5,)

s = (5) # without comma, Python treat this as a normal value 
# print(type(single))
# print(type(s))

#accessing tuple elements
# print(mixed[2])
# print(mixed[-1])

#immutability
# mixed[2] = 23342

#tuple operation
a = (1,2)
b = (3,4)
c = a + b
print(c)


a = (5,6)
print(a * 3)


#membership test
print(5 in a)
print(2 not in a)

#tuple function
print(len(a))
print(min(a))
print(max(a))
print(sum(a))

list = [1,2,3,4,45]
list = tuple(list) # conver the list to tuple
print(type(list))


#tuple packing and unpacking
person = (214, "Debashish Sahu", "bhopal")
# sch_no, name , location = person
# print(sch_no, name, location)


#we can use * for variable length unpacking
sch_no, *other_details  = person
# other_details would be a list of string
print(sch_no, other_details)

#tuple method
t = (1,2,3,2,2,2,5)
print(t.count(2))
print(t.index(3)) #giving the first index of the value in the tuple


# Summary
# Property	Description
# Type	Ordered, immutable collection
# Syntax	( )
# Indexing	Yes (0-based)
# Duplicates	Allowed
# Heterogeneous	Yes
# Nested Tuples	Supported
# Mutability	No (can’t modify)
# Use Case	Fixed data, faster lookups, dictionary keys