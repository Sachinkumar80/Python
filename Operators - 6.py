# Arithmetic Operators
x = 4
y = 2

total = (x+y)
print(total)

total = (x - y)
print(total)

total = (x * y)
print(total)

total = (x/y)
print(total)

total = x % y 
print(total)

total = x**y
print(total)



# COMPARISON OPERATORS 

a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)


# Assignment Operators 

c = 0
d = 1

c+=d # C = C+D 
print(c)

c-=d # C = C-D 
print(c)


# Logical Operators 

# and
# or 
# not - for neglect something

a = 40 
b = 50 

x = 3 
y = 6 

out = (a > b) or (x > y) # Both false 
print(out)

out = (a > b) or (x < y) # 1 false 1 right
print(out)

out = (a < b) or (x < y) # # both right 
print(out)

out = (a > b) and (x > y) # Both false 
print(out)

out = (a > b) and (x < y) # 1 false 1 right
print(out)

out = (a < b) and (x < y) #  both right, means and is very strict 
print(out)

out = not(x < y) # neglect true value into false one.
print(out)


# Memebership Operators 

Tuple = ("IOT", 67, "Ansible", "AWS", 78)
ans = "AWS" in Tuple
print(ans)

Tuple = ("IOT", 67, "Ansible", "AWS", 78)
ans = "AWS" not in Tuple
print(ans)

Tuple = ("IOT", 67, "Ansible", "AWS", 78)
ans = 78 in Tuple
print(ans)

Tuple = ("IOT", 67, "Ansible", "AWS", 78)
ans = 78 not in Tuple
print(ans)

# Identity operators
a = 12
b = 14

result = a is b # reverse of Membership operators, a = b hai
print(result)

result = a is not b #  a /= b not equal to 
print(result)