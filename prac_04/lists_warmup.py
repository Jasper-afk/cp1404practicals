"""CP1404 practical 4 lists warmup tasks."""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] should be 3                                        (yes)
# numbers[-1] should be 2                                       (yes)
# numbers[3] should be 1                                        (yes)
# numbers[:-1] should be [3, 1, 4, 1, 5, 9, 2]                  (close, there is no 2)
# numbers[3:4] should be 1, 5                                   (close, no 5)
# 5 in numbers should be True                                   (yes)
# 7 in numbers should be False                                  (yes)
# "3" in numbers should be False                                (yes)
# numbers + [6, 5, 3] should be [3, 1, 4, 1, 5, 9, 2, 6, 5 ,3]  (yes)

numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])
print(9 in numbers)
