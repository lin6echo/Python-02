basket = ['a','b','c','d','e']

print(basket.index('d')) # hányadik index helyen van 'd'

print(basket.index('d', 0,4)) # 'd' -t keresi a megadott index tarományban

print('d' in basket)    # 'd' benne van a változóban get: True
print('x' in basket)    # get False

print('i' in 'Hi my name is Csaba')     # get True