""" Обход индексов списка"""

coordinates = [0, 1, 3, 2, 0]

for index, value in enumerate(coordinates): #1 - способ
    print(index, value)

for i in range(len(coordinates)): #2 - способ
    print(i)