import sys

sys.stdin = open('sample_input.txt', 'r')

def combination(arr):
    groups = []
    l = len(arr)
    for i in range(2**(l-1)):
        a, b = [], []
        for j in range(l):
            if i & (1 << j):
                a.append(arr[j])
            else:
                b.append(arr[j])
        groups.append((a, b))
        groups.append((b, a))
    return groups
                
for T in range(int(input())):
    result = 1000
    full = 3
    N = int(input())
    board = [tuple(map(int, input().split())) for i in range(N)]
    students = []
    steps = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                students.append((i, j))
            elif board[i][j] >= 2:
                steps.append((i, j, board[i][j]))

    groups = combination(students)

    stepAx, stepAy, stepAd = steps[0]
    stepBx, stepBy, stepBd = steps[1]

    for groupA, groupB in groups:
        time = 1
        distanceA, distanceB = [], []
        for studentA in groupA:
            distance = abs(studentA[0] - stepAx) + abs(studentA[1] - stepAy)
            distanceA.append(distance)
        distanceA.sort()
        for studentB in groupB:
            distance = abs(studentB[0] - stepBx) + abs(studentB[1] - stepBy)
            distanceB.append(distance)
        distanceB.sort()

        queueA, queueB = [], []

        while True:
            if time >= result:
                break

            new_distanceA, new_distanceB = distanceA[:], distanceB[:]

            for k in range(len(distanceA)):
                if distanceA[k] < time:
                    if len(queueA) is full:
                        continue
                    else:
                        queueA.append([distanceA[k], stepAd])
                        new_distanceA.pop(0)
            distanceA = new_distanceA

            for k in range(len(distanceB)):
                if distanceB[k] < time:
                    if len(queueB) is full:
                        continue
                    else:
                        queueB.append([distanceB[k], stepBd])
                        new_distanceB.pop(0)
            distanceB = new_distanceB

            for person_in_stepA in queueA:
                person_in_stepA[1] -= 1
            for person_in_stepB in queueB:
                person_in_stepB[1] -= 1

            new_queueA, new_queueB = [], []

            for person in range(len(queueA)):
                if queueA[person][1] != 0:
                    new_queueA.append([queueA[person][0], queueA[person][1]])
            queueA = new_queueA
            for person in range(len(queueB)):
                if queueB[person][1] != 0:
                    new_queueB.append([queueB[person][0], queueB[person][1]])
            queueB = new_queueB
            time += 1
            if not queueA and not queueB and not distanceA and not distanceB:
                if time < result:
                    result = time
                break

    print('#{} {}'.format(T+1, result))
