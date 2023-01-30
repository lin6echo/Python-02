
# positional parameters
def say_hello(name, emoji):            # name, emoji : parameters
    print(f'hello {name}{emoji}')

# positional arguments
say_hello('Csaba ', ':)')

# keyword arguments
say_hello(emoji=':(', name='Sziszi')

# default parameters
def say_hello(name='Dart Vader', emoji=':)'):
    print(f'Hello {name} {emoji}')

say_hello('Csaba ', ':)')
say_hello()