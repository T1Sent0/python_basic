first_list = input("Введите значения первого списка разделённые запятыми ").split(',')
second_list = input("Введите значения второго списка разделённые запятыми ").split(',')

second_list_to_set = set(second_list)

filtred_list = [item for item in first_list if item not in second_list_to_set]

print("Результат ")
print(filtred_list)