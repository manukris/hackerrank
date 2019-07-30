n = int(input(""))
arr = list(map(int, input().rstrip().split(" ")))
arrw = list(map(int, input().rstrip().split(" ")))

sumw = 0

for x in range(len(arr)):
    sumw = sumw + (arr[x] * arrw[x] )
wmean = round(sumw / sum(arrw),1)
print(wmean)
