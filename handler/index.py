
from handler import BaseHandler


class IndexHandler(BaseHandler):

    def get(self):
        self.write('hello world!')
