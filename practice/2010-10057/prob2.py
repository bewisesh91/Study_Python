# 문제 2: 리스트 합치기

def list_accumulator(num_list) :
    total = 0
    for i in num_list :
        if type(i) == list :
            temp = total
            total = list_accumulator(i) + temp
        else :
            total += i
    return total

