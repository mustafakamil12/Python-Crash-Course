file_name = 'alice.txt'

try:
    with open(file_name) as file_object:
        content = file_object.read()
except FileNotFoundError:
    print(f"Sorry the file {file_name} you trying to open, doesn't exist!")

else:
    words = content.split()
    number_of_words = len(words)
    print(number_of_words)
