""" We are given two numbers. The task is to find the LCM of the numbers."""
a=int(input())
b=int(input())

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

lcm=(a*b)/gcd(a,b)
print(lcm)
