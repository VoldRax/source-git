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
