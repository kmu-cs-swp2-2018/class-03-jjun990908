import time
import random

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def iterfibo(n):
    answer = 1
    temp = 0
    before = 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range (1,n):
            temp = answer
            answer = before + answer
            before = temp
        return answer

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    tm = time.time()
    iterfibonumber = iterfibo(nbr)
    tm = time.time() - tm
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    print("FiboLoop(%d)=%d, time %.6f" % (nbr, iterfibonumber, tm))
