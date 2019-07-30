# Enter your code here. Read input from STDIN. Print output to STDOUT

def calcMedian(arr,n):
    if n % 2 == 0:
        median = (arr[n // 2] + arr[(n // 2) - 1]) // 2
    else:
        n1 = (n - 1) // 2
        median = arr[n1]
    return median

n = int(input(""))

arr = list(map(int,input().split(" ")))


arr.sort()

if (n % 2 == 0):
    n1 = n // 2
    n2 = n1 - 1
    print(calcMedian(arr[:n2], (n2+1)))
    print(calcMedian(arr,n))
    print(calcMedian(arr[n1:], n - n1))
else:
    n1 = (n - 1) // 2
    # print(arr[n1+1:],n - n1)
    print(calcMedian(arr[:n1],(n1)))
    print(calcMedian(arr,n))
    print(calcMedian(arr[n1+1:],(n - n1)-1))
