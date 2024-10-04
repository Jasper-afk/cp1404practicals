"""CP1404 Practical 3 - reading files in 4 different ways."""

# Question 1.

name = input("Your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2.

in_file = open("name.txt", 'r')
name = in_file.read()
print(name)
in_file.close()

# Question 3.

total = 0
with open("numbers.txt", "r") as in_file:
    numbers = in_file.readlines(3)

for number in numbers:
    number.strip()
    total += int(number)
print(total)

# Question 4.

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        line.strip()
        total += int(line)
print(total)
