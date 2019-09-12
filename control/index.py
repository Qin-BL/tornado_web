
from lib.redis import rs


def get_index_content(id):
    res = rs.get('index_content')
    if not res:
        pass
    return res
