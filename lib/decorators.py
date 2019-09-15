
def model_to_dict(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs).__dict__
        del res['_sa_instance_state']
        return res
    return wrapper


def model_to_list(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i in res:
            i.__dict__
            del i['_sa_instance_state']
        return res
    return wrapper
