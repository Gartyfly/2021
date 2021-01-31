x=int(input())
y=int(input())
z=int(input())
if x**2+y**2+z**2>1000:
    w=(x**2+y**2+z**2)//10000
    print(w)
else:
    h=(x+y+z)
    print(h)
