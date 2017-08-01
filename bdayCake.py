import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_h = max(ar)
    rep = ar.count(max_h)
    print(rep)
    return n-rep

ar = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]
result = birthdayCakeCandles(10, ar)
print(result)