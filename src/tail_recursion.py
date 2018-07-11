"""helper class to assist python in deeper tail_recursion
## limit to depth tends to be 1000 recursions
## REF: https://chrispenner.ca/posts/python-tail-recursion"""
class Recurse(Exception):
    """recursion class implementation"""
    def __init__(self, *args, **kwargs):
        """init"""
        self.args = args
        self.kwargs = kwargs
def recurse(*args, **kwargs):
    """Throw away the used stack. Exception manages the actual tail aspect of tail recursion"""
    raise Recurse(*args, **kwargs)

def tail_recursive(funct):
    """method to allow for tail recursion. usage decorate your method with @tail_recursion"""
    def decorated(*args, **kwargs):
        """inner method for making the decorator"""
        while True:
            try:
                return funct(*args, **kwargs)
            except Recurse as recursion:
                args = recursion.args
                kwargs = recursion.kwargs
                continue
    return decorated
