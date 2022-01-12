prompt = "Do you wanna to continue on program if not please enter quit: "
message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
