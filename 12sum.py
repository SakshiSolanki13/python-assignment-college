def sum_of_digits(number):
    
    digit_sum = 0
    
    while number > 0:
        digit = number % 10
   
        digit_sum += digit
        number = number // 10

    return digit_sum

user_input = int(input("Enter an integer: "))

result = sum_of_digits(user_input)
print(f"The sum of digits of {user_input} is: {result}")