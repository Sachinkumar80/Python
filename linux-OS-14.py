#!/usr/bin/python3

import os
filenm = 'test1.txt'
path = '/tmp/test1.txt'
if os.path.isdir(path):
    print (f" Directory with name {filenm} present.")
elif os.path.isfile(path):
    print (f" File with name {filenm} not present.")
else:
    print("file or dir not avilable")

# Adding user into linux 
#!/usr/bin/python3
import os

userlist =  ["alpha", "beta", "gamma"]

print ("###########################")
print ("Adding user to the system")

for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print ("User {} does not exist. Adding it.".format(user))
        print ("######################################")
        print ()
        os.system("useradd {}".format(user))
    else:
        print ("User already exist. skipping it.")
        print ("#################################")
        print ()


# Removing the user from the system
#!/usr/bin/python3
import os

userlist = ["Alpha", "Beta", "Gama"]

print("###########################")
print("Removing users from the system")

for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode == 0:
        print("User {} exists. Removing it.".format(user))
        print("######################################")
        os.system("userdel {}".format(user))
    else:
        print("User {} exists. Removing it.".format(user))
        print("#################################")

# Adding group to the system.
#!/usr/bin/python3
import os

groupname = "science"

print("###########################")
print("Checking if group '{}' exists".format(groupname))

exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group doesn't exists. Adding creation.")
    print("######################################")
    os.system("groupadd science")
else:
    print("Group already exist skiping it")
    print("######################################")

# Adding users into science group.
for user in userlist:
    print ("Adding user {} in the science group".format(user))
    print ("##################################################")
    print()
    os.system("usermod -G science {}".format(user))


# Adding directory and Giving permission to it.

if os.path.isdir("/opt/science_dir"):
    print ("Directory alredy exist, skipping it")
else:
    os.mkdir("/opt/science_dir")
    print ("Directory created successfully")

    print ("Assiging the permission and ownership to the directory")
    print ("########################################")
    print ()
    os.system("chown :science /opt/science_dir")
    os.system("chmod 777 /opt/science_dir")

