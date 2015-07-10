import warnings

def deprecated(func):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.'''
    def new_func(*args, **kwargs):
        if not new_func.__called:
            warnings.warn('Call to deprecated function "{0}".'.format(func.__name__),
                          stacklevel=2)
            new_func.__called = True
        return func(*args, **kwargs)
    new_func.__name__ = func.__name__
    new_func.__doc__ = func.__doc__
    new_func.__dict__.update(func.__dict__)
    new_func.__called = False
    return new_func
