def greet(name):
    print(f"Hello, {name}!")
    """
    2
    This function takes a name as input and prints a greeting message.

    Parameters:
    - name (str): The name of the person to greet.

    Returns:
    None
    """

# Accessing the docstring
if __name__=='__main__':
    print(greet.__doc__)
    greet("Ali Khan")
