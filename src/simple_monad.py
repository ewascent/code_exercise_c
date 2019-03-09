import math

def double(i):
    return i * 2

def Ω(val1):
    """#Ω = lambda x: x"""
    return val1

class Expr:
    def __init__(self, val=None, div=None):
        self.val = val
        self.div = div
    def getVal(self):
        if self.val is None and self.div is None:
            return None
        elif self.val is None:
            return self.div
        elif self.div is None:
            return self.val
        return self.val * self.div

nm = Expr(val=10, div=(1/2))

print("x is " + str(nm.getVal()))


class Pipeline:
    def __init__(self,
                 functions=(),
                 vals=(),
                 terminals=(print,)):
        if hasattr(functions, '__call__'):
            self.functions = [functions]
        else:
            self.functions = list(functions)
        self.input = vals
        self.terminals = [Ω] + list(terminals)

    def __ror__(self, vals):
        self.input = vals
        return self

    def __or__(self, func):
        assert hasattr(func, '__call__')
        self.functions.append(func)
        if func in self.terminals:
            return self.eval()
        return self

    def eval(self):
        vals = []
        for y in self.input:
            for f in self.functions:
                y = f(y)
            vals.append(y)
        return vals

def echo(stringer):
    print(stringer)

statement = 'hello there' |  Pipeline() | echo |  Ω

x = range(5)  |  Pipeline()  | double |  Ω
print(x)

p = Pipeline() | double | math.floor

for num in (range(100, 103),  (11.5,  21.2, -6.7, 34.7), (5, 8, 10.9)):
    result = num | p |  Ω
    print(result)
