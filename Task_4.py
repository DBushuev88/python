n = abs(int(input("Введите целое положительное число ")))
a = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > a:
        a = n % 10
    if n > 9:
        continue
    else:
        print(f"Максимальное цифра в числе, {a} ")
        break