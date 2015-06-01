__author__ = 'User'

numbers = []
count = 0
while True:
    number_user = input('enter a number or Enter to finish: ')
    try:
        number = int(number_user)
        #count += 1
        numbers.append(number)
    except ValueError:
        if number_user == '' and len(numbers) > 0:
            break
        elif number_user == '':
            numbers.append(0)
            break
        else: print("Use only numbers")

summa = sum(numbers)
lowest = min(numbers)
highest = max(numbers)
average = summa / len(numbers)

print('numbers: {0} \n'.format(numbers))
print('count = {0} sum = {1}  lowest = {2}  highest = {3} mean = {4} '.format(count, summa, lowest, highest, average))



