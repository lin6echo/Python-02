def is_even(num):
    if num % 2 == 0:
        return True

    elif num % 2 != 0:
        return False

print(is_even(11))

# better way 1

def is_even(num):
    if num % 2 == 0:
        return True

    else:
        return False

print(is_even(11))

# better way 2

def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(11))

# better way 3

def is_even(num):
    return num % 2 == 0

print(is_even(11))
