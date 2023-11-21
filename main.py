import numpy as np
from _mul import two_multiply
from _sum import two_sum

def main():
    a, b = map(int,input().split(' '))
    _mul = two_multiply(a,b)
    _sum = two_sum(a,b)
    
    answer = _mul / _sum
    print(answer)

if __name__=="__main__":
    main()