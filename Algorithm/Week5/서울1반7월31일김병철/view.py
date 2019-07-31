for i in range(10):
    len_case = int(input())
    test_case = input()[:-1]
    test_list = ['']*len_case
    a = ''
    list_index = 0
    jomang = 0
    j = 1
    for letter in test_case:
        if letter == ' ':
            test_list[list_index] = int(a)
            a = ''
            list_index += 1
        else:
            a += letter
    test_list[list_index] = int(a)
    while j < len_case-2:
        right_left = [test_list[j-2],test_list[j-1],test_list[j+1],test_list[j+2]]  
        maxi = 0
        if test_list[j] > test_list[j-2] and test_list[j] > test_list[j-1] and test_list[j] > test_list[j+1] and test_list[j] > test_list[j+2]:
            for tall in right_left:
                if maxi == 0:
                    maxi = tall
                else:
                    if maxi < tall:
                        maxi = tall
            jomang += test_list[j]- maxi
            j += 3
        else:
            j += 1      
    print('#{0} {1}'.format(i+1,jomang))
            

