import random

numbers = [random.randint(1, 100) for _ in range(20)]

print("Сгенерированный список:", numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("Четные числа из списка:", even_numbers)

divisible_by_3 = [num for num in numbers if num % 3 == 0]
print("Числа, делящиеся на 3:", divisible_by_3)

average = sum(numbers) / len(numbers)
print("Среднее арифметическое всех чисел:",average)
