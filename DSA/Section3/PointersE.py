num1 = 11  # pointing variable to a integer
num2 = num1  # pointing num2 variable to s

print("before num2 value is updated")
print("num1=", num1)
print("num2=", num2)
print("\nnum1's ID = ", id(num1))
print("num2's ID  = ", id(num2))

num2 = 22

print("after num2 value is updated")
print("num1=", num1)
print("num2=", num2)
print("\nnum1's ID = ", id(num1))
print("num2's ID  = ", id(num2))

# now checking other datatype dictionary

dict1 = {
    'value': 11
}
dict2 = dict1

print("before dict2 value is updated")
print("dict1=", dict1)
print("dict2=", dict2)
print("\ndict1's ID = ", id(dict1))
print("dict2's ID  = ", id(dict2))

dict2['value']=22
print("\nafter dict2 value is updated")
print("dict1=", dict1)
print("dict2=", dict2)
print("\ndict1's ID = ", id(dict1))
print("dict2's ID  = ", id(dict2))

# as itegers are immutables 