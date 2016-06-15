# Loops and lists: Its and object in programming that allows you to store value
# Different list based on different data types

lists=['Christopher','Susan','Bill','Santana']
lists[2]='Prajwol'
print(lists)
lists.append('Ojashri')
print(lists)
lists.remove('Christopher')
print(lists[-1])

for names in lists:
    print("Guest Name : " + names)