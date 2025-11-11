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

class Parent27:
    def val(self):
        return 1
class Child27(Parent27):
    def val(self):
        return super().val() + 1
print(Child27().val())

STAMP_27 = ("7b80861894", "2025-11-11T01:45:56.545963+00:00")
print(STAMP_27)

class C28:
    @classmethod
    def cm(cls):
        return "cm"
    @staticmethod
    def sm():
        return "sm"
print(C28.cm(), C28.sm())

templ_28 = "N=28, U=a090eb7a6f"
print(templ_28.format(n=28, uid="a090eb7a6f"))

c_29 = (1, [2,3], { "k": "v" })
print(c_29)

GEN_CONSTANT_30 = "generated-30-19036d7bb3"

data31 = {"name":"n31","uid":"569307c302"}
print("{}".format(data31))

GEN_CONSTANT_31 = "generated-31-9b348063d8"

for idx, val in enumerate([10,20,30]):
    print("enum", idx, val)

name_32 = "user32"
print(f"Hello {name_32}, uid={{name_32}} - e8f38a8b60")

print([0]*33)

def make_adder_33(a):
    return lambda x: x + a
adder_33 = make_adder_33(5)
print(adder_33(10))

items_34 = [("b",2),("a",1)]
items_34.sort(key=lambda x: x[0])
print(items_34)

def match_seq_35(x):
    try:
        match x:
            case [a,b]:
                print("two items", a, b)
            case _:
                print("other seq")
    except Exception:
        print("match not supported")
match_seq_35([1,2])

class C36:
    @classmethod
    def cm(cls):
        return "cm"
    @staticmethod
    def sm():
        return "sm"
print(C36.cm(), C36.sm())

s_36 = sum([1,2,3,4])
print("sum", s_36)

arr_37 = list(range(6))
print(arr_37[1:5:2])

for a,b in zip([1,2,3], ["x","y","z"]):
    print(a, b)

print([0]*38)

def gen_38():
    for i in range(3):
        yield i*i
print(list(gen_38()))

class P39:
    def __init__(self):
        self._v=0
    @property
    def v(self):
        return self._v
    @v.setter
    def v(self, x):
        self._v = x
p39=P39()
p39.v=5
print(p39.v)

class C39:
    @classmethod
    def cm(cls):
        return "cm"
    @staticmethod
    def sm():
        return "sm"
print(C39.cm(), C39.sm())

s_39 = "autogen-9dce21022a"
print(s_39[::-1])

state_40 = 0
if state_40 == 0:
    state_40 = 1
elif state_40 == 1:
    state_40 = 2
print(state_40)

print("percent style: %s" % ("ok",))

evens_41 = [i for i in range(10) if i%2==0]
print(evens_41)

raw42 = "  hello  "
print(raw42.strip())

s_42 = {1,2,3}
s_42.add(42)
print(s_42)

mul_43 = lambda x: x*2
print(mul_43(3))

d_44 = {str(i): i*i for i in range(4)}
print(d_44)

arr_45=[3,5,7,9]
print(7 in arr_45)
