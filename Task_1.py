a = 1
b = 10.0
bool_True = True
bool_False = False
name = "Dmitriy"

q = type(a)
w = type(b)
e = type(bool_True)
r = type(bool_False)
t = type(name)

h = input(f"Как тебя зовут?")
g = input(f"{h} Введите текст: ")

print(f"Типы данных, которые находятся здесь: \n{q},\n{w},\n{e},\n{r},\n{t}")
print(f"Ты ввел(а): {g}")
