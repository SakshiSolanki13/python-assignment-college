def is_multiple_of_5_and_7(number):
    if number % 5 == 0 and number % 7 == 0:
        return True
    else:
        return False


user_input = int(input("Enter an integer: "))

if is_multiple_of_5_and_7(user_input):
    print(f"{user_input} is a multiple of both 5 and 7.")
else:
    print(f"{user_input} is not a multiple of both 5 and 7.")