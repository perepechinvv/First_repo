"""LIST"""

lst = [1, 2, 3, 'a', [1, 2, ['a', 'b', 'c']]]

# print(type(lst))

# print(lst[-2])

lst[0] = 45

# print(lst[-1][-1][1])

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1

lst[0] = 10

# print(lst1)


slc1 = [3, 4, 5, 6]
slc2 = slc1[::-1]

# slc2[0] = 30

# print(slc1, slc2)

lst1 = [1, 2, 3]

lst2 = [4, 5, 6]

print(lst1 + lst2)

lst1.index()