# Conditions and variables 
print ("This IT organisation has various skills sets.")
print ("Find out your match.")

print ("Enter Capitalised Values.")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "K8s", "Terraform"]
Development = ("NodeJS", "AngularJS", "java", ".net", "python")
cntr_empl = {"Name":"Santa", "Skill":"Blockchain", "code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "code":1574}

usr_skill = input("Enter your desired skills: ")
print(usr_skill)

# Check in the database if we have this skill.
if usr_skill in DevOps:
    print(f"We have {usr_skill} in Devops Team.")
elif(usr_skill in Development):
    print(f"We have {usr_skill} in Development Team.")
elif(usr_skill in cntr_empl.values()) or (usr_skill in cntr_empl.values()):
    print(f"We have contract employees with this {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling.")


