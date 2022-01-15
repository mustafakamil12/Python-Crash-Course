file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

# Printing the first 20 digits in the string of course as string
print(pi_string[:20])
