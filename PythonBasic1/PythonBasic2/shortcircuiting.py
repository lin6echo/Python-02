is_Friend = True
is_User = True

print(is_Friend and is_User)

if is_Friend and is_User:
    print('best friends forever')

if is_Friend or is_User:
    print('best friends forever')

is_Friend = False
is_User = True

if is_Friend and is_User:
    print('best friends forever')

if is_Friend or is_User:
    print('best friends forever')