def seperator():
    print('________________')
    
print('hello world')

# variable types/data types

names = "art"
last = "lemus"
age = 28
found = False
average = 2.313



print(names)
print(average)
print(found)


# operations

print(21 + 21)
print(1100 - 46)
print(54 * 65)
print(133 / 5)
print(100 % 5)  # % modulus operator(gives the residue)
 
print(names + names)
print(age + age)
print(names + str(age))  # parse int into a string print(name + str(age) )

seperator()

if (age < 90):
    print('your young')
elif (age == 90):
    print('old ass')
else:
    print('way too old')
