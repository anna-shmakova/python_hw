user_number = int(input('Введите время в секундах: '))
hours = int(user_number // 3600)
minutes = int((user_number % 3600) // 60)
seconds = int((user_number % 3600) % 60)

print(f'{hours}:{minutes}:{seconds}')
