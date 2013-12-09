from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

# David, David & Nathan's solution


# 45 minutes per kg, plus 20 minutes for turkey undIer 4.5kg
# 40 minutes per kg for turkey between 4.5kg and 6.5kg
# 35 minutes per kg for a turkey of more than 6.5kg

def cooking_time(weight):
    if weight < 4.5:
        time = 20 + 45 * weight
    elif ((weight >= 4.5) and (weight <= 6.5)):
        time = 40 * weight
    else:
        time = 35 * weight
    hours = int(time // 60)
    minutes = int(time % 60)
    time_f = "<h1>%s hours %s minutes</h1>" % (hours, minutes)
    return time_f

def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    ret = environ['PATH_INFO'][1:]
    weight = float(ret)
    return str(cooking_time(weight))

httpd = make_server('', 8080, simple_app)
print "Serving on port 8080..."
httpd.serve_forever()

