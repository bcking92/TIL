def solution(k, room_number):
    answer = []
    room = [i for i in range(1, 200001)]
    for i in room_number:
        temp = i
        while True:
            if room[temp - 1] == temp:
                room[temp - 1] += 1
                selected_room = temp
                break
            temp = room[temp - 1]
        answer.append(selected_room)
    return answer


print(solution(10, [1,3,4,1,3,1]))

print([1,3,4,2,5,6])


def solution2(k, stones):
    answer = 99999999
    for i in range(len(stones) - k + 1):
        temp = max(stones[i:i + k])
        if temp < answer:
            answer = temp
    return answer

print('answer = ' + str(solution2(3, [2, 4, 5, 3, 2, 1, 4, 2, 5, 1])))

print('result = ' + '3')