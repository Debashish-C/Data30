#A set is a unordered, muatable and unindexed collection of unique element
fruits = {"apple", "banana", "cherry"}

#we can declair using set also
numbers = set([1,2,2,3,3,3,34]) 
print(numbers)

## important
empty = {} # this create an empty dictionary not a set 
empty = set() #this create a empty set

#accesing element of a set
#we can not access element by numbers[0]
for fruit in fruits:
    print(fruit)

#add() - add a single element
fruits.add("orange")
print(fruits)

#update - add multiple element
fruits.update(["mango", "kitty"])
print(fruits)

## Removing an element
#remove - remove an element if element not in the set than through an error 
fruits.remove("banana")

#discard() - remove an element if not found dont return error
fruits.discard("grape")

#pop() - remove and return an random element
items = fruits.pop()
print(items)
items = fruits.pop()
print(items)

#clear all the element
# fruits.clear()


#Mathematical operation

A = {1,2,3,4,5}
B = {3,5,6,7,7,8}

#Union
print(A | B)
print(A.union(B))

#intersection
print(A & B)
print(A.intersection(B))

#deference
print(A - B)
print(A.difference(B))

#set membership and comparison
A = {1,2,3}
B = {1,2,3,4,5}
print(2 in A)
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint({4,5}))


#reference and Copy
A = {1,2,4}
B = A #same reference
B.add(A)

print(A)

#real copy
B = A.copy()
B.add(34)
print(A, B)


#if we want a set that can not be changed than use immutable set
A = frozenset([1,2,3])
# A.add(4) #produce and error 

#remove duplicate from a list 
nums = [1,2,3,3,3,4,45,5,4]
unique = list(set(nums))
print(unique)