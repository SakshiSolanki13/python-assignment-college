
num_of_numbers = int(input("Enter the number of real numbers: "))

product = 1

for i in range(num_of_numbers):
    num = float(input(f"Enter real number {i + 1}: "))
    product *= num
print(f"The product of the {num_of_numbers} real numbers is: {product}")
