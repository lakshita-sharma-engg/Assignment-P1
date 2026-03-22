# Trace the memory id using different variables and see the location is changed or not 

# Integer data type 

x = 250
print("int before : " + str(id(x)))
x = 80
print("int after : " + str(id(x)))
print("Memory ID of x is changed in Integer\n")

x = 45
print("int before : " + str(id(x)))
x = x + 10
print("int after : " + str(id(x)))
print("Memory ID of x is changed in Addition\n")

x = 70
print("int before : " + str(id(x)))
x = x - 25
print("int after  : " + str(id(x)))
print("Memory ID of x is changed in Subtraction\n")

x = 18
print("int before : " + str(id(x)))
x = x * 1
print("int after  : " + str(id(x)))
print("Memory ID of x may not change if value remains same\n")

x = 27
print("int before : " + str(id(x)))
x = x % 4
print("int after : " , str(id(x)))
print("Memory ID of x is changed in Modulus\n")

# Integer are immutable data types


# Float data type 

y = 6.3
print("float before : " , str(id(y)))

y = 9.4
print("float after : " , str(id(y)))
print("ID of y is changed in Float \n")

y = y + 1.6 
print("float after add operation : " , str(id(y)))

y = y - 3.2
print("float after sub operation : " , str(id(y)))

y = y * 5
print("float after multi operation : " , str(id(y)))

y = y / 2
print("float after div operation : " , str(id(y)))

print("Float is immutable\n")


# List data type

x = [4, 8, 12]
print("ID before : " , id(x))
x.append(16)
print("ID after  : ",  id(x)) 
print("Memory ID of x is not changed in List\n")

x = [7, 14, 21]
print("ID before : ", id(x))
x[1] = 100
print("ID after  : " , id(x))
print("Memory ID of x is not changed in List\n")

# List are mutable data type


# String data type

s = 'Python'
print("ID before : " ,id(s))

s = s + ' Code'
print("ID after  :", id(s))

s = s.upper()
print("ID after upper : ", id(s))

s = s.lower()
print("ID after lower : ", id(s))

s = s.replace("code", "Program")
print("ID after replace : ", id(s))

s = " Python Program "
s = s.strip()
print("ID after strip : " ,id(s))

# String are immutable data type


# Dictionary data type

d = {"Name": "Rahul", "Age": "19"}
print(d)
print("ID before : ", id(d))

d["City"] = "Indore"
print(d)
print("ID after : ", id(d))
print("The address of the dictionary does not change")

# Dictionary are mutable data type