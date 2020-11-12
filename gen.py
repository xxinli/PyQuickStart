from time import sleep

def add1(x, y):
    return x + y

class Addr:
    def __call__(self, x, y):
        return x + y

add2 =  Addr()

def compute():
    rv = []
    for i in range(10):
        sleep(0.5)
        rv.append(i)
    return rv

class Compute:
    def __iter__(self):
        self.last = 0
        return self
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(0.5)
        return rv

for val in Compute():
    print(val)

def compute1():
    for i in range(10):
        sleep(0.5)
        yield i

for val1 in compute1():
    print(val1)

