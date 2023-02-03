class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name        # attributes
            self.age = age

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player2.membership)
