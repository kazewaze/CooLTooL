# Exercise 1
my_list = [8, 20, 5, 5.5, 12, 18, -24, -2, 9, 180]

for list_item in my_list:
    print(list_item)

# Exercise 2
def repeated_division(user_number):
    quo = user_number
    bit_holder = 0
    bits = []

    # This prevents a catastrophe...
    if (user_number == 0):
        print(user_number, '\n')
        print(str(user_number) + ' = ' + str(user_number))
        return

    while (True):
        if (quo != 1):
          bit_holder = quo % 2
          bits.append(bit_holder)
          quo = quo // 2
          print(bit_holder)
        else:
            bits.append(1)
            print(1, '\n')
            bits.reverse()
            print(str(user_number) + ' = ' + ' '.join(str(bit) for bit in bits))
            break

user_input = int(input("Enter a number: "))

repeated_division(user_input)

# Exercise 3
char_str = "Hello world"
char_list = [67, 79, 83, 67, 32, 49, 51, 48, 50]

for char_ in char_str:
    print(ord(char_))

for char_ in char_list:
    print(chr(char_))

# Exercise 4
def repeated_addition(user_numbers):
    result = 0

    if (len(user_numbers) == 3):
        if ((not user_numbers[0].isdigit()) or (not user_numbers[2].isdigit())):
            print("Your input was fishy, try again.")
            return

        user_numbers = [int(user_numbers[0]), int(user_numbers[2])]

        for k in range(0, user_numbers[1]):
            result += user_numbers[0]

        print(result)
        return result
    else:
        print("Your input was fishy, try again.")
        return

user_input = input("Enter two numbers (separated by a space): ")
repeated_addition(user_input)