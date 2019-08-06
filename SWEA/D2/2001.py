for i in range(int(input())):
    square = []
    highscore = 0
    N, M = map(int,input().split())
    for j in range(N):
        square.append(list(map(int,input().split())))
    for j in range(N-M+1):
        for k in range(N-M+1):
                score = 0
                for l in range(M):
                        score += sum(square[j+l][k:k+M])
                if highscore < score:
                        highscore = score
       
    print('#{} {}'.format(i+1, highscore)) 