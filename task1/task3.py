i = int(input('ведите вагон в который сел витя '))
j = int(input('ведите вагон в котором соказался витя '))
if i == j:
    print("без дополнительной  информации решения нет")
else:
    print(f"в поезде всего: {i + j - 1} вагонов")
