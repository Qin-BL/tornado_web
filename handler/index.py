
from handler import BaseHandler
from control import ctrl


class IndexHandler(BaseHandler):

    def get(self):
        self.write('hello world!')
