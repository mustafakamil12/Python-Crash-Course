class Dog:
    """A simple attmpt to model a dog."""

    def __init__(self, name, age):
        """Initilize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to ac command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in respons to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
