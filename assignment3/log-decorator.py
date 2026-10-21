

# Task 1: Writing and Testing a Decorator
# Within the assignment3 folder, create a file called log-decorator.py.  
# It should contain the following.
# Declare a decorator called logger_decorator.  
# This should log the name of the called function (func.__name__), 
# the input parameters of that were passed, and the value the function returns, 
# to a file ./decorator.log.  
# (Logging was described in lesson 1, so review this if you need to do so.)  
# Functions may have positional arguments, keyword arguments, both, or neither.  
# So for each invocation of a decorated function, the log would have the following. 
# Example format — your exact spacing and wording may vary; 
# what matters is that each invocation logs the function name, the positional parameters (or "none"), 
# the keyword parameters (or "none"), and the return value:
# function: <the function name>
# positional parameters: <a list of the positional parameters (as a tuple or a list), or "none" if none are passed>
# keyword parameters: <a dict of the keyword parameters, or "none" if none are passed>
# return: <the return value>
# Here's a setup example on logging (adapt as needed; your logger name may differ):
# # one time setup
# import logging
# logger = logging.getLogger(__name__ + "_parameter_log")
# logger.setLevel(logging.INFO)
# logger.addHandler(logging.FileHandler("./decorator.log","a"))
# ...
# # To write a log record:
# logger.log(logging.INFO, "this string would be logged")
# Declare a function that takes no parameters and returns nothing.  For example, it could print "Hello, World!".  
# Decorate this function with your decorator.
# Declare a function that takes a variable number of positional arguments and returns True.  
# Decorate this function with your decorator.
# Declare a function that takes no positional arguments and a variable number of keyword arguments, 
# and that returns logger_decorator.  
# Decorate this function with your decorator.
# Within the mainline code, call each of these three functions, 
# passing parameters for the functions that take positional or keyword arguments.  
# Run the program, and verify that the log file contains the information you want.


import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {args if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

# function that takes no parameters and returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")

# function that takes a variable number of positional arguments and returns True
@logger_decorator
def return_true(*args):
    return True

# function that takes no positional arguments and a variable number of keyword arguments; returns logger_decorator
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

# calling the functions
say_hello()
return_true(1,13,26)
return_decorator(name = "Eileen", age = 43)