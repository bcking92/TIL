import sys

sys.stdin = open('input.txt', 'r')

def bfs(start):
    global contact
    queue = [[start, 0]]
    visited = {}
    result = []
    temp_max = 0
    depth_dic = {}
    for i in range(0, 101):
        depth_dic[i] = []
    while queue:
        temp = tuple(queue.pop(0))
        depth_dic[temp[1]].append(temp[0])
        visited[temp[0]] = temp[1]
        if contact.get(temp[0]):
            for j in contact[temp[0]]:
                if not visited.get(j):
                    for l in queue:
                        if l[0] == j:
                            break
                    else:
                        queue.append([j, temp[1] + 1])

    for k, v in visited.items():
        if v > temp_max:
            temp_max = v
    # print(visited)
    # print(depth_dic)
    for k, v in visited.items():
        if v == temp_max:
            result.append(k)
    # print(result)
    print('#{} {}'.format(T + 1, max(result)))

for T in range(10):
    N, s = map(int,input().split())
    ll = list(map(int, input().split()))
    contact = {}
    for i in range(0, N, 2):
        if not contact.get(ll[i]):
            contact[ll[i]] = [ll[i+1]]
        else:
            if ll[i+1] not in contact[ll[i]]:
                contact[ll[i]].append(ll[i+1])
    bfs(s)