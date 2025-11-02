numbers = input("Введите числа через пробел:")
numbers_list = numbers.split()
print(numbers_list)
summa = 0
for i in numbers_list:
    summa += int(i)
print("Сумма элементов:", summa)
