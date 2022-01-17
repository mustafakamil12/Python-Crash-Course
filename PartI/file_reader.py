file_name = '/Users/mustafaalogaidi/Desktop/Python-Crash-Course/PartI/pi_digits.txt'
with open(file_name) as file_object:
    contents = file_object.read()

print(contents)
#print(contents.rstrip())
