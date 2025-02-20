
# Creating a list of even numbers
def even_nums(n):
  even_lsts = [item for item in range(0, n) if item % 2 == 0]
  return even_lsts

# Creating a list of odd numbers
def odd_nums(n):
  odd_lsts = [item for item in range(0, n) if item % 2 != 0]
  return odd_lsts

# Creating a list of square numbers
def square_nums(n):
  square_lsts = [item*item for item in range(0, n) ]
  return square_lsts

if __name__ == "__main__":
    even_range = int(input("Enter your limit to generate even numbers : "))
    print ("Even Numbers : ", even_nums(even_range))
    print()

    odd_range = int(input("Enter your limit to generate odd numbers : "))
    print ("Odd numbers : ", odd_nums(odd_range))
    print()

    square_range = int(input("Enter your limit to generate square numbers : "))
    print ("Square numbers : ", square_nums(square_range))
    print()

