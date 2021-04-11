def P1(lst):
    count = 0
    for i in range(len(lst)) :
        for j in range(len(lst)-1) :
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
                count += 1
    return count
