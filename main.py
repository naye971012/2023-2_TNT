import numpy as np


def two_multiply(a:int, b:int) -> int:
    pass

def two_sum(a:int, b:int) -> float:
    pass

def main():
    a, b = map(int,input().split(' '))
    _mul = two_multiply(a,b)
    _sum = two_sum(a,b)
    
    answer = _mul / _sum
    print(answer)

if __name__=="__main__":
    main()