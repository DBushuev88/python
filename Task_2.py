time = int(input("Введите время в секундах "))
hours = time // 3600
minutes: int = (time - hours * 3600) // 60
seconds: int = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")