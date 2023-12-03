class Dog():
    # Initializer / Instance Attributes
    def __init__(self, name_of_the_dog):
        print("A new dog has been initialized !")
        print("His name is", name_of_the_dog)

shelter_dog = Dog(name_of_the_dog="Rex")
# or
shelter_dog = Dog("Rex")

shelter_dog.color='Brown'

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

first_person = Person("John", 36)

print(first_person.name)
print(first_person.age)

class Computer():

    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")