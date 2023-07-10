# Break Statement:

# Example of using break statement in a for loop

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# Pass Statement:

# Example of using pass statement in a loop

for i in range(5):
    if i == 3:
        pass
    else:
        print(i)

# Continue Statement:

# Example of using continue statement in a while loop

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# For loop with Else Statement:

# Example of using for loop with else statement

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    if fruit == 'orange':
        break
    print(fruit)
else:
    print("No more fruits left!")

# While loop with Else Statement:

# Example of using while loop with else statement

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop completed!")






