"""
Dictionary Concepts from Basics to Advanced
Author: Santosh Gawande
"""

# ----------------------------------------
# 🔹 1. Dictionary Creation and Access
# ----------------------------------------
d = {}        # using literal
d1 = dict()   # using constructor

d["one"] = 1
print("Basic dict creation:", d)

d2 = {'one': 1, 'two': 2, 'three': 4, 6: 'six'}
print("Access with int key:", d2[6])


# ----------------------------------------
# 🔹 2. Properties of Dictionary Keys
# ----------------------------------------
d = {True: 'yes', 1: 'no', 1.0: 'maybe'}
print("Conflicting keys:", d)  # {True: 'maybe'}
print("Why? Because True == 1 == 1.0:", True == 1 == 1.0)



# ----------------------------------------
# 🔹 3. Dictionary Operations
# ----------------------------------------
dict1 = {"key": "value", "name": "san", "age": 20}
print("Access name:", dict1['name'])

for k in dict1:
    print(f"{k}: {dict1[k]}")

for idx, key in enumerate(dict1):
    print(f"{idx}: {key}")

for k, v in dict1.items():
    print(f"{k} => {v}")

print("Keys:", list(dict1))

# Insert/update/delete
d1 = {}
d1['h'] = 'hello'
print("Insert single key:", d1)

d2 = {'key': 'value'}
d2['key'] = 'high'
print("Updated value:", d2)

del dict1['key']
print("After deletion:", dict1)

print("'key' in dict1?", 'key' in dict1)


# ----------------------------------------
# 🔹 4. Advanced: Dictionary Comprehensions
# ----------------------------------------
d3 = {x: x * x for x in (2, 3, 4, 5, 6)}
print("Dict comprehension:", d3)


# ----------------------------------------
# 🔹 5. First-Class Functions with Dictionary (Switch Case Emulation)
# ----------------------------------------
def myfunc(a, b):
    return a + b

print("Normal function:", myfunc(4, 5))

funcs = [myfunc]
print("First-class function:", funcs[0](2, 3))

# Emulating switch-case
switch = {
    'sum': lambda x, y: x + y,
    'diff': lambda x, y: x - y
}
print("Switch 'sum':", switch['sum'](10, 5))



# ----------------------------------------
# 🔹 6. Common Mistakes and Invalid Operations
# ----------------------------------------
# Note: d.insert(...) is NOT valid
# d = {}
# d.insert({'key': 2, 'h': 5})  # ❌ This will raise an error

# ----------------------------------------
# 🔹 7. Extra: Creating from sequence
d4 = dict([(1, 6), (7, 8)])
print("Dict from sequence:", d4)
