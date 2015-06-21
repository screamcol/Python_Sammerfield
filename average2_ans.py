__author__ = 'Kirshak Yauheni'

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

sort_list = []

#min = numbers[0]
#max = numbers[0]

#for i in numbers:
#    if i > max:
#        max = i
#for i in numbers:
#    if i < min:
#        min = i

while True:
    minimum = min(numbers)
    #maximum = max(numbers)
    sort_list.append(minimum)
    numbers.remove(minimum)
    if len(numbers) == 1:
        sort_list.append(numbers[0])
        break


count = len(sort_list)
summa = sum(sort_list)
lowest = min(sort_list)
highest = max(sort_list)
average = summa / len(sort_list)

if len(sort_list) % 2 != 0:
    middle_of_list = len(sort_list)//2
    mediana = sort_list[middle_of_list]
else:
    middle_low = sort_list[(len(sort_list)//2) - 1]
    middle_high = sort_list[(len(sort_list)//2)]
    mediana = (middle_low + middle_high) / 2


print('numbers: {0} \n'.format(sort_list))
print('count = {0} sum = {1}  lowest = {2}  highest = {3} mean = {4} mediana {5}'.format(count, summa, lowest, highest, average, mediana))

