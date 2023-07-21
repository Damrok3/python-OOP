# exception =   events detected during execution that interrupt the flow of a program.

try:
    numerator = int(input("enter a number to divide: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero idiot")
except ValueError as e:
    print(e)
    print("Enter only numbers pls")
except Exception as e:
    print(e)
    print("something went wrong :<")
else: 
    print(result)
finally:
    print("This will always execute")
