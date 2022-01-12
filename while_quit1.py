prompt = "Do you wanna to continue on program if not please enter quit: "

active = True # This is flag will be used in program
while active:
    message = input(prompt)

    if message == "quit":
        print("Bye Bye!")
        active = False
    elif message == "stop":
        break
    else:
        print(message)
