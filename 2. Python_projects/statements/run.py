# -*- coding: utf-8 -*-
# /run.py
from app import create_app


app = create_app()

# точка входа
if __name__ == '__main__':
    print(__file__)
    app.run(host='0.0.0.0', port='80')
