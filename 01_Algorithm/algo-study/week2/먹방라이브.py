def solution(food_times, k):
    answer = 0
    len_food_times = len(food_times)
    new_len_food_times = len_food_times
    new_food_times = [(food_times[i], i + 1) for i in range(len_food_times)]
    sorted_food_times = sorted(new_food_times, key=lambda x: x[0])
    
    set_food_times = tuple(set(food_times))
    now_minus = 0
    if k >= len_food_times * set_food_times[now_minus]:
        k -= len_food_times * (set_food_times[now_minus] - 1)
        for i in range(set_food_times[now_minus], sorted_food_times[-1][0]+1):             
            if k >= len_food_times:
                if i == set_food_times[now_minus]:
                    for j in range(len_food_times):
                        if sorted_food_times[0][0] == i:           
                            sorted_food_times.pop(0)
                            new_len_food_times -= 1
                        else:
                            break
                    now_minus += 1
                k -= len_food_times                                     
                len_food_times = new_len_food_times           
            else:
                fin_sorted_food_times = sorted(sorted_food_times, key=lambda x: x[1])
                return fin_sorted_food_times[k][1]
        else:
            return -1
    else:
        return k % len_food_times + 1

print(solution([3,1,2], 5))
print(solution([4,3,3,1,1], 5))
print(solution([5,1,1], 5))
print(solution([3,3,3], 8))
print(solution([1,2,3,4], 1))