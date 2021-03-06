# -*- coding: utf-8 -*-

"""
    Blah blah
"""

import os
import jinja2
from eve import Eve

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'


app = Eve()

if __name__ == '__main__':
    app.run(host=host, port=port)
