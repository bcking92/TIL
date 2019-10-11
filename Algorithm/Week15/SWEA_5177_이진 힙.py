for T in range(int(input())):
    N = int(input())
    arr = tuple(map(int, input().split()))
    heap = [0]
    result = 0
    for i in range(len(arr)):
        heap.append(arr[i])
        if i > 0:
            temp_i = i+1
            while True:
                if heap[temp_i//2] > heap[temp_i]:
                    heap[temp_i], heap[temp_i//2] = heap[temp_i//2], heap[temp_i]
                    temp_i = temp_i//2
                    if temp_i == 1:
                        break
                else:
                    break
    while True:
        N = N//2
        result += heap[N]
        if N == 1:
            break
    print('#{} {}'.format(T+1, result))