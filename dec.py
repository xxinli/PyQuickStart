from time import time

def timer(func, x, y):
    before = time()
    rv = func(x,y)
    after = time()
    print('elapsed:', after - before)
    return rv

def timer1(func):
    # def f(x, y=10):
    def f(*args, **kwargs):
        before = time()
        # rv = func(x,y)
        rv = func(*args, **kwargs)
        after = time()
        print('elapsed:', after - before)
        return rv
    return f

def add(x , y=10):
    return x + y

@timer1
def sub(x , y=10):
    return x - y
# sub=timer1(sub)

print('add(10', timer(add, 10, 1))
print('sub(10)', sub(12,9))