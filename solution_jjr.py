from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import re
import json


# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    headers = [('Content-type', 'application/json')]

    mo = re.match(r'/(\d+(\.\d*)?)', environ['PATH_INFO'])

    if mo is not None:
        status = '200 OK'
        start_response(status, headers)
        time_in_mins = turkey_time(float(mo.group(1)))
        val = {'hours': int(time_in_mins // 60), 'minutes': int(time_in_mins % 60)}
        return json.dumps(val)

    status = '404 Not Found'
    start_response(status, headers)
    return 'Error'


def turkey_time(weight):
    """
    Returns the longest cooking time suggested for a given weight.

    :param weight: The weight of the turkey in kilograms.
    """
    return max([(weight * 45) + 20, (weight * 40) + 20, (weight * 35) + 20])

httpd = make_server('', 8000, simple_app)
print("Serving on port 8000...")
httpd.serve_forever()