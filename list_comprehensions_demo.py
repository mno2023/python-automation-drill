
# Creating a list of even numbers
n = 10
even_nums = [item for item in range(0, n) if item % 2 == 0]
print ("Even_nums : ", even_nums)

# Creating a list of odd numbers
n = 10
odd_nums = [item for item in range(0, n) if item % 2 != 0]
print ("Odd_nums : ", odd_nums)


# Creating a list of square numbers
n = 10
square_nums = [item*item for item in range(0, n) ]
print ("Square_nums : ", square_nums)
