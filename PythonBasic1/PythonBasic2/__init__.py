class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (age > 18):
            self.name = name        # attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player2.membership)
player2.attack = 50

print(player2.shout())