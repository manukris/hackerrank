n = int(input(""))
x = list(map(int,input("").split(" ")))
mean = sum(x) / n
print(round(mean,1))
x.sort()
n = len(x)
if n % 2 == 0:
    midval = n // 2
    median = (x[midval] + x[midval - 1]) / 2
    print(round(median,1))
else:
    midval = (n - 1) // 2
    print(round(midval,1))
countlist = []
for i in x:
    countlist.append(x.count(i))
if sum(countlist) == n:
    print(x[0])
else:
    print(x[countlist.index(max(countlist))])
