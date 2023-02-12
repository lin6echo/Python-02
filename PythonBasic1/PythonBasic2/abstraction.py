class PlayerCharacter:
    def __init__(self, name, age):
            self.name = name        # attributes
            self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old.')

player1 = PlayerCharacter('Csaba', 58)
player1.speak()
print((1,2,3,1).count(1))
print(len((1,2,3,1)))
