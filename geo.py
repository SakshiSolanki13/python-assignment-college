def calculate_geometric_mean(numbers):
    product = 1

    for num in numbers:
        product *= num

    geometric_mean = product ** (1 / len(numbers))
    return geometric_mean

n = int(input("Enter the number of elements: "))


numbers = []
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

result = calculate_geometric_mean(numbers)
print(f"The geometric mean of the entered numbers is: {result}")