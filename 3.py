n = int(input("Введите число n: "))

print("Числа от n до 1 в обратном порядке:")
current = n
while current >= 1:
    print(current, end=' ')
    current -= 1
print()

print("Факториал числа n:")
factorial = 1
current = 1
while current <= n:
    factorial *= current
    current += 1
print(factorial)
