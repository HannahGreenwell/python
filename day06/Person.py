class Person:

    def __init__(self, name="Reginald"):
        print('Creating new Person with name', name)
        self.name = name

    def greet(self):
        print('Hello, I am', self.name)

    def laugh(self):
        print('Ha ha ha!')

class Comedian(Person):

    def __init__(self, name):
        print('Creating new Person with name', name)
        self.name = name

    def tell_joke(self):
        print('Knock knock...')

    # def laugh(self):
    #     print('Ha ha! Nice joke bro')

    def laugh(self):
        super().laugh()
        print('Nice joke bro!')

frederick = Person('frederick')
frederick.greet()
frederick.laugh()

reg = Person()
reg.laugh()
