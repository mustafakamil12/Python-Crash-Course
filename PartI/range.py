for value in range(5):
    print(value)

print("\n")
for newvalue in range(1,5):
    print(newvalue)

newlist = list(range(1,6))
print(newlist)

even_numbers = list(range(2,11,2))
print(even_numbers)

exp_list = []
for element in range(11):
    exp_list.append(element ** 2)
print(exp_list)

sequares = [com_value ** 2 for com_value in range(1,11)]
print(f"sequares = {sequares}")

my_fam = ['mustafa','farouq','muhanned','inaam']
print(my_fam)
print(my_fam[1::2])

new_fam = my_fam

my_fam.append('Kamil')
new_fam.append('Thuraya')
print(f"my_fam = {my_fam}")
print(f"new_fam = {new_fam}")

tup_fam = ('mustafa','farouq')
#tup_fam[0] = 'muhanned'
tup_fam = ('muhanned','inaam')
print(tup_fam)
