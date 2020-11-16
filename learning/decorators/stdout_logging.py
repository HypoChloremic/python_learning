from functools import wraps

def stdout_log(func):
    '''stdout_log() will print statements
    upon entering and exiting a function, outputting the names of the 
    functions that are being called'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[{func.__name__}] Entering')
        result = func(*args, **kwargs)
        print(f'[{func.__name__}] Exiting')
        return result
    return wrapper


@stdout_log
def randomfunc(printhtis='hello'):
    return printthis

class RandomClass:
    def __init__(self):
        pass

    @stdout_log
    def class_method(self):
        return 'random class method'

if '__main__' == __name__:
    rn = RandomClass()
    rn.class_method()