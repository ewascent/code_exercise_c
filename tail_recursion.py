## helper class to assist python in deeper tail_recursion
## limit to depth tends to be 1000 recursions
## REF: https://chrispenner.ca/posts/python-tail-recursion
class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)

# usage decorate your method with @tail_recursion
def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as recursion:
                args = recursion.args
                kwargs = recursion.kwargs
                continue
    return decorated
