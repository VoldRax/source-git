str = '0-:-m]#th}5 k$;(d+{j'+k#]ju[:# *6rkiygri<nu?}_ff?u?9z_q4sy1}y;(*&'
print(str)

arr_1=[3,5,7,9]
print(7 in arr_1)

class It2:
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
print(list(It2(3)))

pairs_2 = [(i, j) for i in range(3) for j in range(2)]
print(pairs_2)

arr_3 = list(range(6))
print(arr_3[1:5:2])

def f1_4(x):
    return x+1
def f2_4(x):
    return x*2
print(f2_4(f1_4(3)))

nested_5 = [[1,2],[3,4]]
flat_5 = [x for sub in nested_5 for x in sub]
print(flat_5)

lst2_6 = [1,2]
lst2_6.extend([3,4])
lst2_6.pop(0)
print(lst2_6)

def deco_7(f):
    def wrapper(*a, **k):
        print("before")
        r=f(*a, **k)
        print("after")
        return r
    return wrapper
@deco_7
def targ_7():
    print("target")
targ_7()

s_8 = {1,2,3}
s_8.add(8)
print(s_8)

d_9 = {'a':1,'b':2}
for k,v in d_9.items():
    print(k, v)

class M10:
    def mix(self):
        return "mixed"
class X10(M10):
    pass
print(X10().mix())

lst10 = ["a","b"]
d10 = {i:lst10[i] for i in range(len(lst10))}
print(d10)

def fib_10(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
print(list(fib_10(15)))

class A11: pass
class B11: pass
class C11(A11, B11): pass
print(C11.__mro__)

lst_11 = [3,1,2]
lst_11.sort()
print(lst_11)

d_12 = {'a':1,'b':2}
for k,v in d_12.items():
    print(k, v)

def is_prime_13(x):
    if x<2: return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True
print(is_prime_13(13))

s14 = "radar"
print(s14 == s14[::-1])

ns_14 = [{"i":i, "s":[j for j in range(i)]} for i in range(3)]
print(ns_14)

def make_adder_15(a):
    return lambda x: x + a
adder_15 = make_adder_15(5)
print(adder_15(10))

class P16:
    def __init__(self):
        self._v=0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, x):
        self._v = x
p16=P16()
p16.v=5
print(p16.v)

ns_16 = [{"i":i, "s":[j for j in range(i)]} for i in range(3)]
print(ns_16)

class GenClass17:
    def __init__(self):
        self.id = "01d73f3a85"
    def show(self):
        print("GenClass17 id:", self.id)
obj_17 = GenClass17()
obj_17.show()

print("Generated statement #18 uid=0151567ecd ts=2025-11-11T01:36:16.233872+00:00")

m_18 = [[1,2],[3,4]]
print(list(zip(*m_18)))

def deco_19(f):
    def wrapper(*a, **k):
        print("before")
        r=f(*a, **k)
        print("after")
        return r
    return wrapper
@deco_19
def targ_19():
    print("target")
targ_19()

class C20:
    @classmethod
    def cm(cls):
        return "cm"
    @staticmethod
    def sm():
        return "sm"
print(C20.cm(), C20.sm())

items_20 = [("b",2),("a",1)]
items_20.sort(key=lambda x: x[0])
print(items_20)

print("percent style: %s" % ("ok",))

def fib_21(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
print(list(fib_21(15)))

class D22:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f"D22(a={self.a}, b={self.b})"
print(D22(1,2))

pairs_22 = [(i, j) for i in range(3) for j in range(2)]
print(pairs_22)

class D23:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f"D23(a={self.a}, b={self.b})"
print(D23(1,2))

print(hex(23))

arr23 = [1,2,3]
for i in range(len(arr23)-1):
    print(arr23[i], arr23[i+1])

lst2_23 = [1,2]
lst2_23.extend([3,4])
lst2_23.pop(0)
print(lst2_23)

class C24:
    @classmethod
    def cm(cls):
        return "cm"
    @staticmethod
    def sm():
        return "sm"
print(C24.cm(), C24.sm())

name_24 = "user24"
print(f"Hello {name_24}, uid={{name_24}} - 5ee1607290")

arr_25 = list(range(6))
print(arr_25[1:5:2])

lst_26 = [3,1,2]
lst_26.sort()
print(lst_26)

try:
    1/0
except ZeroDivisionError:
    print("caught div by zero")
