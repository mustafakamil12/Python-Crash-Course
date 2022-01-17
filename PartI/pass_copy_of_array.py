def pass_copy(cp_list):
    cp_list.append(100)
    print(f"cp_list = {cp_list}")


my_list = [1,2,3,4,5,6]
pass_copy(my_list[:])
print(f"my_list = {my_list}")
