user_input = input()
binary_list = user_input.split(",")
for number in binary_list:
    if int(number, 2) % 5 == 0:
        print (number)
