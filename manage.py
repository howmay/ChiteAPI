# -*- coding: utf-8 -*-
from chite.application import create_app
import os

app = create_app(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run()
