country = input('Your country: ')
age = input('How old are you? ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('You can drive')
	else:
		print('You cannot drive')
elif country == 'Japan':
	if age >= 20:
		print('You can drive')
	else:
		print('You cannot drive')
elif country == 'Ameria':
	if age >= 16:
		print('You can drive')
	else:
		print('You cannot drive')
else:
	print('Taiwan/Japan/Ameria')