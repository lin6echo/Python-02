name = 'Bajzáth Csaba'
age = 58
relationship_status = 'married'

relationship_status = 'it\'s complicated'

print(relationship_status)

from datetime import date
current_year = date.today().year
print(current_year)

birth_year = input('what year were you born')

age = current_year - int(birth_year)
print(f'Your age is {age}')
