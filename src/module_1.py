def nested_diveide_numbers(n,m):
    try:
        result=n/m     
    except ZeroDivisionError as e:
        print("Denominator cannot be 0 \nError:",e)
    except TypeError as e:
        print("Numerator and Denominator can only be Integers \nError:",e)
    else:
        print(f"{n}/{m}={result}")
    finally:
        print("Divide Function Execution Completed!\n")

def divide_numbers(numerator,denominator):
    try:
        result=numerator/denominator
        nested_diveide_numbers("7",3)     
    except ZeroDivisionError as e:
        print("nested_Denominator cannot be 0 \nError:",e)
    except TypeError as e:
        print("nested_Numerator and Denominator can only be Integers \nnested_Error:",e)
    else:
        print(f"nested_{numerator}/{denominator}={result}")
    finally:
        print("nested_Divide Function Execution Completed!\n")

if __name__=='__main__':
    divide_numbers("5",4)