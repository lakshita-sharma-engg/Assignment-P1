# Checking memory ID changes with different values

#  INTEGER 
print(" INTEGER")

a = 200
print("Before:", id(a))
a = 75
print("After :", id(a))
print("→ Memory ID changed\n")

a = 90
print("Before:", id(a))
a = a + 5
print("After :", id(a))
print("→ Memory ID changed (Addition)\n")

a = 45
print("Before:", id(a))
a = a - 10
print("After :", id(a))
print("→ Memory ID changed (Subtraction)\n")

a = 12
print("Before:", id(a))
a = a * 2
print("After :", id(a))
print("→ Memory ID changed (Multiplication)\n")

a = 22
print("Before:", id(a))
a = a % 5
print("After :", id(a))
print("→ Memory ID changed (Modulus)\n")


# FLOAT
print("FLOAT")

b = 7.2
print("Before:", id(b))

b = 9.8
print("After :", id(b))
print("→ Memory ID changed\n")

b = b + 3.3
print("After Addition:", id(b))

b = b - 2.1
print("After Subtraction:", id(b))

b = b * 5
print("After Multiplication:", id(b))

b = b / 2
print("After Division:", id(b))

print("→ Float is immutable\n")


#  LIST 
print(" LIST ")

c = [10, 20, 30]
print("Before:", id(c))
c.append(40)
print("After :", id(c))
print("→ Memory ID did NOT change (append)\n")

c = [5, 15, 25]
print("Before:", id(c))
c[1] = 100
print("After :", id(c))
print("→ Memory ID did NOT change (update)\n")


#  STRING
print("STRING ")

s = "Python"
print("Before:", id(s))

s = s + " Code"
print("After Concatenation:", id(s))

s = s.upper()
print("After Upper:", id(s))

s = s.lower()
print("After Lower:", id(s))

s = s.replace("code", "Program")
print("After Replace:", id(s))

s = "  Python Program  "
s = s.strip()
print("After Strip:", id(s))

print("→ Strings are immutable\n")


# DICTIONARY 
print(" DICTIONARY")

d = {"Name": "Rahul", "Age": "19"}
print("Before:", id(d))

d["City"] = "Indore"
print("After :", id(d))

print("→ Memory ID did NOT change\n")