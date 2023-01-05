# https://www.acmicpc.net/problem/1920 백준 1920번 binary search


N = int(input())

list_N = list(map(int, input().split()))
list_N.sort()
M = int(input())

list_M = list(map(int, input().split()))

def binary_search(target, data) :
    start = 0
    end = len(data)-1

    while start <= end :
        mid = (start + end) // 2

        if data[mid] == target :
            return True
        elif data[mid] < target :
            start = mid + 1
        else :
            end = mid -1


for i in range(M):
    if binary_search(list_M[i], list_N) :
        print("1")
    else :
        print("0")

