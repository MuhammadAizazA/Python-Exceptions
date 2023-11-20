def divide_numbers(numerator,denominator):
    try:
        result=numerator/denominator
    except ZeroDivisionError as e:
        print("Denominator cannot be 0 \nError:",e)
    except TypeError as e:
        print("Numerator and Denominator can only be Integers \nError:",e)
    else:
        print(f"{numerator}/{denominator}={result}")
    finally:
        print("Divide Function Execution Completed!\n")
    
if __name__=='__main__':
    divide_numbers(10,2)