"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
import math
def Gcd(A,B):
    for i in (B,0,-1):
        if(A%i==0 and B%i==0):
            return i
def gcd(A,B):
    if(A>B):
        return Gcd(A,B)
    else:
        return Gcd(B,A)

print(gcd(12,6))
