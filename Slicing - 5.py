## Slicing example

os = "Linux Redhat Operating system"
print(os[1])
print(os[2])
print(os[3])

# Negative indexing start from end of words 
print(os[-1])
print(os[-2])
print(os[-3])

# Slicing a string, get a substring from a string 
print(os[0:5])
print(os[:11])
print(os[:])
print(os[29:])

# Slicing Tuple
DevOps = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")
print(DevOps[0])
print(DevOps[4])
print(DevOps[-1])

print(DevOps[2:5])
print(DevOps[2:5][0])

print(DevOps[2:5][0][5:11][-1]) # Now you can't slice it more further ! 

# Slicing List
DevOps = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]
print(DevOps[0])
print(DevOps[4])
print(DevOps[-1])

print(DevOps[2:5])
print(DevOps[2:5][0])

print(DevOps[2:5][0][5:11][-1]) # Now you can't slice it more further ! 

# Dictionary Example

skills = {"DevOps": ("AWS", "Jenkins", "Python", "Ansible"), "Development": ["Java", "NodeJS", ".net"]}
print(skills)
print(skills["DevOps"])
print(skills["DevOps"][1:3])
print(skills["DevOps"][-1][:7])
