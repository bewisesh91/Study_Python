# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.


# for i in range(test_case) :
#     N = int(input())
#     lst = sorted(list(map(int, input().split(' '))))
#     new_lst = []
#     new_lst.append(lst.pop())
#     for j in range(1, N) :
#         if lst[0] > new_lst[j-1] :
#             new_lst.append(lst.pop())
#         else : 
#             new_lst.append(lst.pop(0))
#     print(f'#{i+1} {" ".join(list(map(str, new_lst[:10])))}')

test_case = int(input())

for i in range(test_case) :
    N = int(input())
    lst = list(map(int, input().split(' ')))
    new_lst = []
    while len(lst) > 0 :
        new_lst.append(max(lst))
        new_lst.append(min(lst))
        lst.remove(max(lst))
        lst.remove(min(lst))
    print(f'#{i+1} {" ".join(list(map(str, new_lst[:10])))}')
