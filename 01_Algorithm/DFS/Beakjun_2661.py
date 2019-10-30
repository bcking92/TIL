def dfs(arr, x, K, result, length):
    global visited
    global goal
    global go
    if not go:
        return
    if length > 1:
        for m in range(1, length//2 + 1):
            if result[length-m:] == result[length-2*m:length-m]:
                break
        else:
            if x == K:
                go = 0
                print(''.join(map(str,result)))
            else:
                x += 1
                for i in range(3):
                    # if not visited[i]:
                        # visited = [0 for k in range(3)]
                    visited[i] = 1
                    result.append(arr[i])
                    dfs(arr, x, K, result, length + 1)

                    # 위로 올라갈때 해줘야 될 것들은 여기 아래에 써버림 = dfs 더이상 안으로 안들어 갈 때,
                    result.pop()
                    visited[i] = 0
    else:
        x += 1
        for i in range(3):
            # if not visited[i]:
            #     visited = [0 for k in range(3)]
            visited[i] = 1
            result.append(arr[i])
            dfs(arr, x, K, result, length + 1)
            result.pop()
            visited[i] = 0

N = int(input())
memoization = []
visited = [0 for i in range(3)]
num = [1, 2, 3]
goal = []
go = 1
dfs(num, 0, N, memoization, 0)


# 1. result 값을 밖에있는 변수에 할당하고 싶은데 모르겠음
# 2. go 변수를 함수의 파라미터로 넣고싶은데 모르겠음

