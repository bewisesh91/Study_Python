def P2(lst):
    for i in range(len(lst)) :
        for j in range(len(lst)-1) :
            if len(lst[j]) > len(lst[j+1]) :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    for i in range(len(lst)-1) :
        if len(lst[i]) == len(lst[i+1]) :
            lst2 = []
            lst2.append(lst[i])
            lst2.append(lst[i+1])
            lst2.sort()
            lst[i], lst[i+1] = lst2[0], lst2[1]

    return lst
