is_old = True
is_licenced = True

if is_old:
    print('you are old enough to drive!')       # first condition is True therefor ignore the rest
elif is_licenced:
    print('you can drive now!')
else:
    print('check')

is_old = False
is_licenced = True

if is_old:
    print('you are old enough to drive!')       # first condition is False jump the next True condition
elif is_licenced:
    print('you can drive now!')                 # this is True therefore ignore the last one
else:
    print('you are not of age!')

is_old = True
is_licenced = True

if is_old:
    print('you are old enough to drive!')       # first two conditions is False jump the last one       
elif is_licenced:
    print('you can drive now!')                
else:
    print('you are not of age!')

if is_old and is_licenced:
    print('you are old enough to drive, and you have a licence!')       # use and keyword both condition have to be True            
else:
    print('you are not of age!')

