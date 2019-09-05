def combi(x, end):
    global visited, team1, team2, teamset
    if x == end:
        if sum(visited) == N//2:
            for i in range(N):
                if visited[i] == 1:
                    team1.append(member[i])
                else:
                    team2.append(member[i])
            teamset.append((team1, team2))
            team1 = []
            team2 = []
    else:
        visited[x] = 1
        combi(x + 1, end)

        visited[x] = 0
        combi(x + 1, end)


N = int(input())
power = []
member = []
team1 = []
team2 = []
teamset = []
visited = [0] * N

result = 100000
for i in range(N):
    power.append(tuple(map(int, input().split())))
    member.append(i)

combi(0, N)
for i in teamset:
    stat1 = 0
    stat2 = 0
    for j in i[0]:
        for k in i[0]:
            stat1 += power[j][k]
    for j in i[1]:
        for k in i[1]:
            stat2 += power[j][k]
    temp = abs(stat1 - stat2)
    if temp < result:
        result = temp

print(result)
