# Scope - what variables do I have access to?

a = 1                       # Global scope

def confusion():
    a = 5                   # Local scope
    return a

print(confusion())
print(a)

# 1 - start with local

a = 1                      

def confusion():                 
    return a

print(confusion())
print(a)

# 2 - Parent local (Global scope)

a = 1                      

def parent():

    def confusion():                 
        return a
    return confusion()

print(parent())
print(a)

# 3 - Global

a = 1                      

def parent():
    def confusion():                 
        return sum
    return confusion()

print(parent())
print(a)

# 4 - Built in Python function