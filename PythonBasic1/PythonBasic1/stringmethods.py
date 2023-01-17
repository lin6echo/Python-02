quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be')) # 3 azaz a 3-as index helyen találta meg
print(quote.replace('be', 'me'))

# immutable = megváltozhatatlan

print(quote)

quote2 = quote.replace('be', 'me')
print(quote2)