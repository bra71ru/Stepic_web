def wsgi_app(environ, start_response):

    #body = b'Hello\n'

    # 'QUERY_STRING': 'a=1&a=2&b=3'
    body = environ['QUERY_STRING'].replace('&','\n')

    start_response("200 OK", [("Content-Type", "text/plain")])
    return [ body ]

