from collections import deque
import sys

input = sys.stdin.readline

queue = deque([])
result = []
n_input = int(input())

for _ in range(n_input) :

    list_line = input().split()

    if(list_line[0] == "push") :
        #print(list_line[1])
        queue.append(list_line[1])
    elif(list_line[0] == "pop") :
        if(len(queue) == 0) :
            print(-1)
            # result.append(-1)
        else :
            print(queue.popleft())
            # result.append(queue.popleft())
            
    elif(list_line[0] == "size") :
        print(len(queue))
        # result.append(len(queue))
    elif(list_line[0] == "empty") :
        if(len(queue) == 0) :
            print(1)
            # result.append(1)
        else :
            print(0)
            # result.append(0)
    elif(list_line[0] == "front") :
        if(len(queue) == 0) :
            print(-1)
            # result.append(-1)
        else :
            print(queue[0])
            # result.append(queue[0])

    elif(list_line[0] == "back") :
        if(len(queue) == 0) :
            print(-1)
            # result.append(-1)
        else :
            print(queue[-1])
            # result.append(queue[-1])


# for k in result :
#     print(k)

# from collections import deque
# import sys

# input = sys.stdin.readline

# n = int(input())

# q = deque([])

# for _ in range(n):
#     query = input().split()
#     if query[0] == 'push':
#             q.append(query[1])
#     elif query[0] == 'pop':
#         if len(q):
#             print(q.popleft())
#         else:
#             print(-1)
#     elif query[0] == 'size':
#         print(len(q))
#     elif query[0] == 'empty':
#         if len(q):
#             print(0)
#         else:
#             print(1)
#     elif query[0] == 'front':
#         if len(q):
#             print(q[0])
#         else:
#             print(-1)
#     elif query[0] == 'back':
#         if len(q):
#             print(q[-1])
#         else:
#             print(-1)