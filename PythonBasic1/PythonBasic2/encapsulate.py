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

# .........................................................................................
class PlayerCharacter:
    def __init__(self, name, age):
            self.name = name        # attributes
            self.age = age

player1 = PlayerCharacter('Csaba', 58)
print(player1.name)
print(player1.age)

player2 = {'name' : 'Sziszi', 'age' : 54}
print(player2['name'])
print(player2['age'])