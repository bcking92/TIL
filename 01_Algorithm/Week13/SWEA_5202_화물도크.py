for T in range(int(input())):
    N = int(input())
    process_time = []
    result = 1
    for i in range(N):
        process_time.append(tuple(map(int, input().split())))
    process_time = sorted(process_time, key=lambda x : (x[1], x[0]))

    now_end = process_time[0][1]
    for i in range(1, len(process_time)):
        if now_end > process_time[i][0]:
            continue
        else:
            now_end = process_time[i][1]
            result += 1
    print('#{} {}'.format(T + 1, result))