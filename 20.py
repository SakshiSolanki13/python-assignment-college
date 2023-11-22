def sum_of_numbers(n):
    
    numbers = []

  
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    total_sum = sum(numbers)

   
    print(f"Sum of the numbers: {total_sum}")

n = int(input("Enter the value of n: "))

sum_of_numbers(n)