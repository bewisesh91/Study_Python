# 문제 1: 최대공약수

def gcd(num_list) :
    result = []
    for i in range(len(num_list)) :
        temp_result = []
        for j in range(len(num_list)) :
            a = num_list[i]
            b = num_list[j]
            if b > a :
                (a , b) = (b, a)
            while b != 0 :
                (a, b) = (b, a % b)
            temp_result.append(a)
        result.append(temp_result)
    return result