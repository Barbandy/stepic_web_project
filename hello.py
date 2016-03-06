def app(environ, start_response): 
    #logic
    data = environ["QUERY_STRING"]
    data = "\n".join(data.split("&"))
    status = '200 OK'
    heders = [
    ('Content-Type', 'text/plain'),
    ('Content-Lenght', str(len(data))),
    ]
    start_response(status,headers)
    return [data]