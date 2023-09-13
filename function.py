def fac (x):
    if x == 1:
        return 1
    else:
        return (x*fac(x-1))

num = 4
print("factorial of number ",num,"is",fac(num))