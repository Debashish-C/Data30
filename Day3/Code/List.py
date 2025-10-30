#List in Python

# creating a list
numbers = [10,20,30,40,50]

#accessing in list
# print(numbers[6]
# print(numbers)
# print(numbers[0])
# print(numbers[-1])
# print(numbers[-2])

#slices in a list 
# print(numbers[1:3])
# print(numbers[::3]) #numbers of indexes pass and print the list
# print(numbers[3:])

#chaning list element
# numbers[3] = 50
# print(numbers)
# numbers[0:3] = [11,12,13,14] 
# print(numbers)

#adding element to list

#append() -- take exactly one element
# numbers.append(70)
# print(numbers)

# insert -  insert element at a specific index
# numbers.insert(2,100)
# print(numbers)

#extend() - add multiple elements
# numbers.extend([500,600,8006])
# print(numbers)

# removing an element

# numbers.remove(400) #the value should be in list other wise it will give an error
# numbers.append(11)
# print(numbers)
#remove() - remove first occurence of an element
# numbers.remove(11)
# print(numbers)
#pop - remove element by indexes return the element
# numbers.pop()
# print(numbers)
# numbers.pop()
# print(numbers)
#del - delete element by indexes or slice
# del numbers[2:4]
# print(numbers)
#clear() - removes all the elements
# numbers.clear()
# print(numbers)

#searching

# print(numbers)
# print(10 in numbers) #return true or false based on if the value is present in list or not 
# numbers.append(20)
# numbers.insert(8,20)
# print(numbers.index(20)) #return the first index
# print(numbers.count(20))
# print(numbers)


#searching and sorting
# numbers[1] = 500
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

#copying the list
# numbers2 = numbers.copy()
# print(numbers2)

#List comprehension
# squeares = [x**2 for x in numbers]
# print(squeares)


#iterating over a list
# for i,val in enumerate(numbers):
#     print(i, val)

# Commong Wrong thing 
# list1 = [1,2,3]
# list2 = list1 #remember does not create a new list instead point to the same list1
# list1.append(4)
# print(list2)

#soln 
# list3 = list1.copy()
# list1.append(4)
# print(list3)


#dont remove element while iterating it will shift index and sometimes can generate a new error
num  = [1,23,23,3.3,3]
for n in num:
    if(n % 3 == 0):
        num.remove(n)
print(num) #sometimes give wrong answer

#iterating with a copy or you can use list comprehension also 
num.insert(2,33)
num.insert(9,123) #insert value at the last if index not found
print(num)
# for n in num[:]:
#     if n % 3 == 0:
#         num.remove(n)
# print(num)
 
num = [n for n in num if n % 3 != 0]
print(num)


#using mutable object as defgault arguments
def add(v, list = []):
    list.append(v)
    return list
print(add(1))
print(add(2)) #expented only [2] not [1,2]
print(add(5,[10,20]))

#solution
def add_ele(i, lst = []):
    if lst is None:
        lst = []
    lst.append(i)
    return lst
print(add_ele(5))
print(add_ele(10,[44]))


# for 2d list use a.deepcopy() instead of normal copy a.copy()