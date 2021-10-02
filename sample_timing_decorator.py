import time

def timer(function):
    def wrapper():
        start_time = time.time()
        func = function()
        end_time = time.time()
        return end_time - start_time
    return wrapper

@timer
def a_function():
    time.sleep(0.5)
    print('something is happening')

print(a_function())
    
