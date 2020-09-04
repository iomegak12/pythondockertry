def decorator(f):
    def wrap_call(*args, **kargs):
        print('Decorator ...')
        f()
        print('Completed!')

    return wrap_call


def x():
    print('Doing something!')


f = decorator(x)

f()