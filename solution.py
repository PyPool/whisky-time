"Christmas turkey cooking time web application."

from wsgiref.simple_server import make_server


def cooking_mins(size_in_kg):
    if size_in_kg < 4.5:
        factor = 45
    elif size_in_kg < 6.5:
        factor = 40
    else:
        factor = 35
    return (size_in_kg * factor) + 20


def application(environ, start_response):
    path = environ["PATH_INFO"]
    size_in_kg = float(path.strip("/ "))
    mins = cooking_mins(size_in_kg)
    hours, mins = divmod(mins, 60)
    start_response("200 OK", [('Content-Type', "text/plain")])
    return ["{0} hours {1} minutes".format(hours, mins)]


if __name__ == "__main__":
    httpd = make_server('localhost', 8000, application)
    print "Serving on port 8000..."
    httpd.serve_forever()

