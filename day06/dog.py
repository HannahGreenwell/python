class Dog:
    # Keyword that allows an empty class
    # pass
    dog_count = 0
    # constructor function for this class
    def __init__(self, name, roundness):
        # if not type(name) == str:
        #     print('Please use a string for "name"')
        #     raise TypeError
        print('Creating a new instance of Dog:', name, roundness)
        Dog.dog_count += 1
        self.name = name
        self.roundness = roundness

    def describe(self):
        print('Name of dog', self.name)
        print('Roundness of dog', self.roundness)

    def bark(self, bark_count = 1):
        bark_output = "Woof! I am " + self.name + ' '
        print(bark_output * bark_count)

fido = Dog('Fido', 2)
rex = Dog('Rex', 6)
