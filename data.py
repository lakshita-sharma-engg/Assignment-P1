# Trace memory ID of different data types and check if it changes or not

# ------------------ INTEGER ------------------
print("----- INTEGER -----")

x = 100
print("Before:", id(x))
x = 50
print("After :", id(x))
print("→ Memory ID changed\n")

x = 60
print("Before:", id(x))
x = x + 1
print("After :", id(x))
print("→ Memory ID changed (Addition)\n")

x = 35
print("Before:", id(x))
x = x - 20
print("After :", id(x))
print("→ Memory ID changed (Subtraction)\n")

x = 29
print("Before:", id(x))
x = x * 1
print("After :", id(x))
print("→ Memory ID may remain same if value doesn't change\n")

x = 15
print("Before:", id(x))
x = x % 2
print("After :", id(x))
print("→ Memory ID changed (Modulus)\n")

# Conclusion: Integers are immutable


# ------------------ FLOAT ------------------
print("----- FLOAT -----")

y = 4.5
print("Before:", id(y))

y = 5.67
print("After :", id(y))
print("→ Memory ID changed\n")

y = y + 2
print("After Addition:", id(y))

y = y - 4
print("After Subtraction:", id(y))

y = y * 10
print("After Multiplication:", id(y))

y = y / 10
print("After Division:", id(y))

print("→ Float is immutable\n")


# ------------------ LIST ------------------
print("----- LIST -----")

x = [1, 2, 3]
print("Before:", id(x))
x.append(4)
print("After :", id(x))
print("→ Memory ID did NOT change (append)\n")

x = [1, 2, 3]
print("Before:", id(x))
x[0] = 100
print("After :", id(x))
print("→ Memory ID did NOT change (update)\n")

# Conclusion: Lists are mutable


# ------------------ STRING ------------------
print("----- STRING -----")

s = "Hello"
print("Before:", id(s))

s = s + " World"
print("After Concatenation:", id(s))

s = s.upper()
print("After Upper:", id(s))

s = s.lower()
print("After Lower:", id(s))

s = s.replace("world", "Sanya")
print("After Replace:", id(s))

s = " Hello World "
s = s.strip()
print("After Strip:", id(s))

print("→ Strings are immutable\n")


# ------------------ DICTIONARY ------------------
print("----- DICTIONARY -----")

d = {"Name": "Sanya", "Age": "20"}
print("Before:", id(d))

d["City"] = "Ujjain"
print("After :", id(d))

print("→ Memory ID did NOT change\n")

# Conclusion: Dictionaries are mutable