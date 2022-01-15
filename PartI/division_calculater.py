print("to quit program press q anytime")
while True:
    first_number = input("Please enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Please enter second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
