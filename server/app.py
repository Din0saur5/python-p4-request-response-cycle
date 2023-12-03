#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''<h1>The host for this page is {host}</h1>
                <h2>The name of this application is {appname}</h2>
                <h3>The path of this application on the user's device is {g.path}</h3>'''
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


# Hooks are best implemented as decorators. There are four types of hooks:

# @app.before_request: runs a function before each request.
# @app.before_first_request: runs a function before the first request (but not subsequent requests).
# @app.after_request: runs a function after each request.
# @app.teardown_request: runs a function after each request, even if an error has occurred.

# from flask import redirect==>
# @app.route('/reginald-kenneth-dwight')
# def index():
#     return redirect('names.com/elton-john')
