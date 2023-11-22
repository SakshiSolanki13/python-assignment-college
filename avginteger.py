
num_of_integers = int(input("Enter the number of integers: "))

total = 0
for i in range(num_of_integers):
    num = int(input(f"Enter integer {i + 1}: "))
    total += num

average = total / num_of_integers

print(f"The average of the {num_of_integers} integers is: {average}")
