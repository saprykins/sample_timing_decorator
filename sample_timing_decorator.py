#! /usr/bin/env python

import time
def timer(function):
    # This is an example of decorator.
    # It calculates time of a function's cycle
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"It took {end_time - start_time:.2f} seconds to run a function")
    return wrapper


@timer
def a_function():
    # This is a sample function that should be replaced by your function
    time.sleep(0.5)
    print('a function does something')


@timer
def a_function():
    # This is a sample function that should be replaced by your function
    time.sleep(0.5)
    print("a function does something")

if __name__ == "__main__":
    print(a_function())
