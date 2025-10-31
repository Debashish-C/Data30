# function is a block of code that perform a specific task, can take input, and can return output
#default argument
def greet(boss = "Debashish"):
    print("Hello", boss)

greet()
greet("Bossi")


#key word arguments
def greet(name,  msg):
    print(f"Hello {name}, {msg}")

greet(msg="Hii bro", name="Debashish")

# * for  variable length argument
def add_numbers(*args):
    return sum(args)

print(add_numbers(1,2,3,3,4,4,5))

# f** for multiple keyword argument 
def show_info(**krgs):
    for key, value in krgs.items():
        print(key, value)

show_info(name = "Debashish", age = 22, roll = 214)


count = 5
# def incre():
#     count+=1

# incre()
print(count)

def decre():
    global count # use it to acces global other wise it though an error
    count-=1

decre()
print(count)


squares = lambda x:x*x
print(squares(55))


