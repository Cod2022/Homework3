

list1 = [1.2, 3.6, 5.17, 2.3, 10.19]
list2 = []
c = 0
for i in list1:
    d = list1[c] * 100 % 100
    e = round(d, 2)
    f = e / 100
    list2.append(f)
    c += 1
    print(list2)
sum = max(list2) + min(list2)
# result = sum / 100

print(sum)