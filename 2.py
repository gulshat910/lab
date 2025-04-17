n = int(input("Введите число n: "))

print("Числа от 1 до", n, ":")
for i in range(1, n + 1):
    print(i, end=' ')
print()

print("Квадраты чисел от 1 до", n, ":")
for i in range(1, n + 1):
    print(i ** 2, end=' ')
print()

sum_numbers = 0
for i in range(1, n + 1):
    sum_numbers += i
print("Сумма чисел от 1 до", n, ":", sum_numbers)
