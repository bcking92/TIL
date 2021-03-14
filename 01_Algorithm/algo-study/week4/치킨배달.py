def combination(arr, num):
    """
    @param arr 리스트
    @param num 몇개를 뽑을지
    @returns 경우의 수의 배열을 리턴
    """
    result = []
    for i in range(2 ** len(arr)):
        temp = []
        for j in range(len(arr)):
            if i & (1 << j):
                temp.append(arr[j])
        if len(temp) == num:
            result.append(temp[:])
    return result

N, M = map(int, input().split())
chicken_places = []
houses = []
result = 999999
for i in range(N):
    a = input().split()
    for j in range(N):
        if a[j] == '1':
            houses.append([i,j])
        elif a[j] == '2':
            chicken_places.append([i,j])

selected_chicken_places_com = combination(chicken_places, M)
for selected_chicken_places in selected_chicken_places_com:
    now_min = 0
    for house in houses:
        temp_min = 99999
        for selected_chicken_place in selected_chicken_places:
            temp = abs(house[0] - selected_chicken_place[0]) + abs(house[1] - selected_chicken_place[1])
            if temp < temp_min:
                temp_min = temp
        now_min += temp_min
    if now_min < result:
        result = now_min
print(result)
    
