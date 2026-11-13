def func(a,b):
    if a ** b <= 64:
        return 1
    else:
        return 0

x = func(4,3)
y = func(3,4)
a = func(-5, -6) # (-5) ** (-6) = 1/(-5)**6 = 1/15625 = 0.000064
z = [bool(x), bool(y), bool(a)] # boolでは空か0はFalse、1以上はTrueになる
print(z)