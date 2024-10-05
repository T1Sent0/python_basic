count_element = input('Введите количество элементов в списке - ')

counter = 1
list_elements = list()
while counter != (int(count_element) + 1):
    list_elements.append(input('Введите значение для элемента ' + str(counter) + ' '))
    counter += 1

print('Ваш список')
print(list_elements)