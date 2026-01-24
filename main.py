class Parent{n}:
    def val(self):
        return 1
class Child{n}(Parent{n}):
    def val(self):
        return super().val() + 1
print(Child{n}().val())
class P{n}:
    def __init__(self):
        self._v=0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, x):
        self._v = x
p{n}=P{n}()
p{n}.v=5
print(p{n}.v)
try:
    1/0
except ZeroDivisionError:
    print("caught div by zero")
class A{n}: pass
class B{n}: pass
class C{n}(A{n}, B{n}): pass
print(C{n}.__mro__)
print(hex({n}))
def deco_{n}(f):
    def wrapper(*a, **k):
        print("before")
        r=f(*a, **k)
        print("after")
        return r
    return wrapper
@deco_{n}
def targ_{n}():
    print("target")
targ_{n}()
def f1_{n}(x):
    return x+1
def f2_{n}(x):
    return x*2
print(f2_{n}(f1_{n}(3)))
nested_{n} = [[1,2],[3,4]]
flat_{n} = [x for sub in nested_{n} for x in sub]
print(flat_{n})
obj_{n} = { "id": "{uid}", "ts":"{ts}" }
print(repr(obj_{n}))
def gen_{n}():
    for i in range(3):
        yield i*i
print(list(gen_{n}()))
class It{n}:
    def __init__(self, n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i>=self.n:
            raise StopIteration
        self.i+=1
        return self.i-1
print(list(It{n}(3)))
def is_prime_{n}(x):
    if x<2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True
print(is_prime_{n}(13))
arr_{n}=[3,5,7,9]
print(7 in arr_{n})
class CM{n}:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, exc, val, tb):
        print("exit")
with CM{n}():
    print("inside context")
print({n} << 1, {n} >> 1)
d_{n} = {str(i): i*i for i in range(4)}
print(d_{n})
class P{n}:
    def __init__(self):
        self._v=0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, x):
        self._v = x
p{n}=P{n}()
p{n}.v=5
print(p{n}.v)
arr_{n}=[3,5,7,9]
print(7 in arr_{n})
for a,b in zip([1,2,3], ["x","y","z"]):
    print(a, b)
print("Generated statement #{n} uid={uid} ts={ts}")
obj_{n} = { "id": "{uid}", "ts":"{ts}" }
print(repr(obj_{n}))
for idx, val in enumerate([10,20,30]):
    print("enum", idx, val)
items_{n} = [("b",2),("a",1)]
items_{n}.sort(key=lambda x: x[0])
print(items_{n})
class Parent{n}:
    def val(self):
        return 1
class Child{n}(Parent{n}):
    def val(self):
        return super().val() + 1
print(Child{n}().val())
d_{n} = {'a':1,'b':2}
for k,v in d_{n}.items():
    print(k, v)
d{n} = {}
print(d{n}.get('missing', 'def'))
print({n} << 1, {n} >> 1)
class Base{n}:
    def who(self):
        return "base"
class Sub{n}(Base{n}):
    def who(self):
        return "sub"
print(Sub{n}().who())
print(True and False, True or False, not False)
ns_{n} = [{"i":i, "s":[j for j in range(i)]} for i in range(3)]
print(ns_{n})
s_{n} = sum([1,2,3,4])
print("sum", s_{n})
lst2_{n} = [1,2]
lst2_{n}.extend([3,4])
lst2_{n}.pop(0)
print(lst2_{n})
