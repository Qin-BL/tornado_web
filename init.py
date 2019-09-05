#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tornado import web
import tornado.ioloop
from tornado.httpserver import HTTPServer
from tornado.options import options, define
import logging
from settings import *

define('port', default=8888)
define('debug', default=False)
options.parse_command_line()

urls = []


class Application(web.Application):
    pass


if __name__ == '__main__':
    app = Application()
    httpserver = HTTPServer(app, xheaders=True)
    httpserver.listen(options.port)
    logging.info('running..., port=%d, debug=%s' % (options.port, options.debug))
    tornado.ioloop.IOLoop.instance().start()

