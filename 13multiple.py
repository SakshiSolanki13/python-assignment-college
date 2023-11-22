def sum_of_digits(number):

    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number = number // 10
    return digit_sum

for num in range(100, 201):
    if num % 3 == 0:  
        digit_sum = sum_of_digits(num)
        if digit_sum % 2 == 0:  
            print(f"{num} (Sum of digits: {digit_sum})")