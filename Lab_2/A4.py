a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
result = [a, b][a <= b]
print("Наибольшее число:", result)