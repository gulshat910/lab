a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
max_num = max(a, b, c)
min_num = min(a, b, c)
all_equal = a == b == c
print("Наибольшее число:" ,max_num)
print("Наименьшее число:", min_num)
print("Все числа равны" if all_equal else "Числа не равны")
