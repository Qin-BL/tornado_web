
def model_to_dict(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).__dict__
    return wrapper


def model_to_list(func):
    def wrapper(*args, **kwargs):
        return [i.__dict__ for i in func(*args, **kwargs)]
    return wrapper
