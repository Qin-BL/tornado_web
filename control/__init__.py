
from control.redis import rs
import mysql


class Ctrl(object):

    def __init__(self):
        self.redis = rs
        self.mysql = mysql


ctrl = Ctrl
