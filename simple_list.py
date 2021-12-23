names = ['mustafa','farouq','mohanned']
names_temp = names[0]
greetings = f"Hello {names_temp}"
my_list = ['bentely','rolls royce','mybach']

print(greetings)
names_temp = names[1]
greetings = f"Hello {names_temp}"
print(greetings)
names_temp = names[2]
greetings = f"Hello {names_temp}"
print(greetings)

print(my_list)
my_list.append('mezzarati')
print(my_list)

my_list.insert(1,'toyota crown')
print(my_list)

del my_list[3]
print(my_list)

poped_elem = my_list.pop()
print(poped_elem)
print(my_list)

new_poped_elem = my_list.pop(1)
print(my_list)

my_list.remove('bentely')
print(my_list)