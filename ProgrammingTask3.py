a = 1.5
b = a * 100
c = b % 100
d = 10.01
e = d * 100
f = e % 100
print(b)
print(c)
print(e)
print(f)
g = c + f
print(g)

print()

list1 = [1.2, 3.6, 5.0, 2.3, 10.19]
c = 0
for i in range(len(list1)):
    d = list1[c] * 100 % 100
    e = round(d, 2)
    f = e / 100
    c += 1
    print(f)