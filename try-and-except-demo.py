"""
Demo on try-and-except block 
Python3
"""

def division_operation(value_1, value_2):

    try:
        result = value_1 / value_2
        print("Result : ", result)
    except ZeroDivisionError as e:
        print (str(e))

    finally:
        print("Executed the try and except block.")


if __name__ == "__main__":

    division_operation(10, 0)
