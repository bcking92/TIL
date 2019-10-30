# 조합으로 뽑기
import itertools


def select(x):
    global visited, chicken, temp_chic, total_min, result, houses

    if x == len(chicken):
        if sum(visited) == M:
            total_min = 0
            for g in houses:
                now_min = 100
                for l in temp_chic:
                    now = abs(g[0] - l[0]) + abs(g[1] - l[1])
                    if now < now_min:
                        now_min = now
                total_min += now_min
            if total_min < result:
                result = total_min
    else:
        if not visited[x]:
            visited[x] = 1
            temp_chic.append(chicken[x])
            select(x + 1)

            temp_chic.pop()
            visited[x] = 0
            select(x + 1)


dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


N, M = map(int, input().split())
city = [tuple(map(int, input().split())) for _ in range(N)]
result = 10000000000
chicken = []
houses = []
# selected = []
temp_chic = []

# 치킨집 생성
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))

visited = [0] * len(chicken)
# 집 좌표 생성
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))

# 치킨집 수가 M이랑 같을 때
if len(chicken) == M:
    result = 0
    for j in houses:
        temp_min = 100
        for k in chicken:
            temp = abs(j[0] - k[0]) + abs(j[1] - k[1])
            if temp < temp_min:
                temp_min = temp
        result += temp_min

# 치킨집 수가 M보다 클 때
else:
    select(0)
    # a = tuple(itertools.combinations(chicken, M))
    # for j in a:
    #     total_min = 0
    #     for k in houses:
    #         temp_min = 100
    #         for l in j:
    #             temp = abs(k[0] - l[0]) + abs(k[1]- l[1])
    #             if temp < temp_min:
    #                 temp_min = temp
    #         total_min += temp_min
    #     if total_min < result:
    #         result = total_min
print(result)


