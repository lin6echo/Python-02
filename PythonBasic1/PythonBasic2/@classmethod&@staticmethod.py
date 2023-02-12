class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (age > 18):
            self.name = name        # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 21)
player3 = PlayerCharacter.adding_things(2,3)

# print(player1.name)
# print(player2.membership)
# player2.attack = 50

# print(player2.shout())
print(PlayerCharacter.adding_things(2,3))
print(player3)