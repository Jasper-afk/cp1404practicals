for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a.
for i in range(0, 100 + 1, 10):
    print(i, end=' ')
print()

# Question b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question c.
number_of_stars = int(input("Enter a number: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

# Question d.
number_of_stars = int(input("Enter a number: "))
for i in range(number_of_stars):
    for j in range(i + 1):
        print("*", end="")
    print()
print()
