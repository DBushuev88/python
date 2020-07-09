my_list = [4, 512, 8, 32, 16, 128, 32, 64, 128, 256]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')