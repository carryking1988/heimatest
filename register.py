def register(func):
    def wrapper(*args,**kwargs):
        print('hello')
        return wrapper(*args,**kwargs)
    return wrapper
