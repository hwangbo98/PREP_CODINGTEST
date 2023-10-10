#백준 2163번 초콜릿 자르기 

N, M = map(int, input().split())

result = (N-1)*M + M-1
print(result)