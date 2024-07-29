# For loop:
Planet = "Earth"
for sachin in Planet:
    print ("Value of I Is now", sachin)


User = ("Sachin", "seema", "guddan", "tannu")
for peo in User:
    print ("my family memeber is", peo)

# While loop
import time
x = 0
while x <= 10:
    print("Value of X is", x)
    print("Looping")
    x+=1
    time.sleep(1)
    print ("Ok! While loop executed.")
    
    
# Nested loop, loops inside loop
User = ("Sachin", "seema", "guddan", "tannu")
for peo in User:
     print("")
     print ("my family memeber is")
     for i in peo:
          print(i)
