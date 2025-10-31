#A dictionary is a key value pairs
#it is unordered, mutable and indexed by value (Not position like list)
#creating dictionary
person = {
    "name" : "Debashish",
    "age" : 22
}

status = dict(name="server_error", code = "400")

#empty dict
data = {}
#accessing value
print(status["name"])
print(status.get("age")) #use get if u unsure about if the key exist or not 

#adding and updating
status["status"] = "accept"

#deleting element
del person["age"]
status.pop("status") # remove and return the status
status.clear() #remove all the element
# del person # delete dictionary entirely
 
student = {"name " : "Dev", "scholar_number" : "24204031214","course " : "MCA"}
#iterating through a dictionary
for key in student:
    print(f"{key},  {student[key]}")


for key, value in student.items():
    print(f"{key}, {value}")

#Common Dictionary methods
student.keys() # return all the keys
student.values() # return all the values
student.items() #return key value pair
student.get("roll", "N/A")
student.pop("name")
a = {
    "name " : "hey"
}
b = {}
a.update(b)

b = a.copy() #return the shallow copy 


data = {[1, 2, 3]: "list"}  # ❌ TypeError
data = {(1, 2, 3): "tuple"}  # ✅ Works

person = {"a": 1, "b": 2, "c": 3}

for key in person:
    del person[key]   # ❌ RuntimeError
for key in list(person.keys()):
    del person[key]
