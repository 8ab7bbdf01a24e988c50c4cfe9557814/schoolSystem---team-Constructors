Ts so ahh. make it better
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Created Person: {self.name}, Age: {self.age}")

    def set_name(self, new_name):
        self.name = new_name
        print(f"Name updated to {self.name}")

    def set_age(self, new_age):
        self.age = new_age
        print(f"Age updated to {self.age}")


create_name = input("What is their name?: ")
age = int(input("What is their age?: "))
person_instance = Person(create_name, age)


while True:
    command = input("\nEnter a command (info, setname, setage, quit): ").lower()
    
    if command == "info":
        person_instance.info()
    elif command == "setname":
        new_name = input("Enter the new name: ")
        person_instance.set_name(new_name)
    elif command == "quit":
        print("Goodbye!")
        break
    elif command == "setage":
        new_age = int(input("Enter the new age: "))
        person_instance.set_age(new_age)
    else:
        print("Unknown command. Try 'info', 'setname', or 'quit'.")
