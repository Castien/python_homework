

# Task 2: A Decorator that Takes an Argument
# Within your assignment3 folder, write a script called type-decorator.py.
# Declare a decorator called type_converter. It has one argument called type_of_output, 
# which would be a type, like str or int or float. 
# It should convert the return from func to the corresponding type. 
# Example — this illustrates the conversion; adapt it inside your wrapper:
# x = func(*args, **kwargs)
# return type_of_output(x)
# Write a function return_int() that takes no arguments and returns the integer value 5. 
# Decorate that function with type_converter. 
# In the decoration, pass str as the parameter to type_converter.
# Write a function return_string() that takes no arguments and returns the string value "not a number". 
# Decorate that function with type_converter. 
# In the decoration, pass int as the parameter to type_converter. 
# Think: What's going to happen?
# In the mainline of the program, add the following (use exactly as written — this verifies your decorator):
# y = return_int()
# print(type(y).__name__) # This should print "str"
# try:
#    y = return_string()
#    print("shouldn't get here!")
# except ValueError:
#    print("can't convert that string to an integer!") # This is what should happen


def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# function return_int() that takes no arguments and returns the integer value 5. 
# decorated with type_converter, passes str as the parameter to type_converter.
@type_converter(str)
def return_int():
    return 5

# function return_string() that takes no arguments and returns the string value "not a number". 
# decorated with type_converter, passes int as the parameter to type_converter.
@type_converter(int)
def return_string():
    return "not a number"

# testing functions, verifies decorator
y = return_int()
print(type(y).__name__)
try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")