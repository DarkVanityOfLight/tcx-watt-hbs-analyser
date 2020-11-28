# /usr/bin/python3

# Imports
import time

# Variable declarations

# Classes

# Functions

# Decorators
def benchmark_exec_time(func):
    def timer(*args, **kwargs):
        pre_exec = time.clock()

        func(*args, **kwargs)

        after_exec = time.clock()

        print("Function {} needed {} to execute".format(func, after_exec - pre_exec))

    return timer

def get_mem_pos(func):
    def get_pos(*args, **kwargs):
        print(func)

        func(*args, **kwargs)

    return get_pos


# Main

if __name__ == "__main__":
    pass
