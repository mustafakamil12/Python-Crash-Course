def count_word(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"Sorry the file {filename} you trying to open, doesn't exist!")
    else:
        words = content.split()
        number_of_words = len(words)
        print(f"The file {filename} has about {number_of_words} words.")


filenames = ['alice.txt', 'siddhartha.txt', 'little_women.txt']

for filename in filenames:
    count_word(filename)
