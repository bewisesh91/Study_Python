def P5(lst):
    count = 0
    decrease = len(lst)
    while sorted(lst) != lst and decrease != 0:
        temp = max(lst[:decrease])
        lst.remove(temp)
        lst[:decrease].append(temp)
        count += 1
        decrease -= 1

    return count
