import random

with open('numbers.txt', 'w') as file:
    for _ in range(100):
        file.write(str(random.randint(1, 1000)) + '\n')

even_numbers = []
odd_numbers = []

with open('numbers.txt', 'r') as file:
    for line in file:
        num = int(line.strip())
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

with open('even.txt', 'w') as file:
    for num in even_numbers:
        file.write(str(num) + '\n')

with open('odd.txt', 'w') as file:
    for num in odd_numbers:
        file.write(str(num) + '\n')

def print_stats(numbers, file_name):
    count = len(numbers)
    total = sum(numbers)
    average = total / count if count > 0 else 0
    print(f"Файл {file_name}:")
    print(f"  Количество чисел: {count}")
    print(f"  Сумма чисел: {total}")
    print(f"  Среднее арифметическое: {average:.2f}\n")

print_stats(even_numbers, 'even.txt')
print_stats(odd_numbers, 'odd.txt')
