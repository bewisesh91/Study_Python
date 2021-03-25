# 문제 2: 리스트 합치기

list_1 = [1, 2, 3]
list_2 = [1, [2, 3], [[4]]]


def list_accumulator(num_list) :
    
    total = 0
    for i in num_list :
        
        if type(i) == list :
            temp = total
            list_accumulator(i)

        else :
            total += i
    
            
    return total

print(list_accumulator(list_2))
