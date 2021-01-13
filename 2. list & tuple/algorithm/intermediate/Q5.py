# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.


# test_case = 3
# area = 2

# data1 = '2 2 4 4 1'
# data2 = '3 3 6 6 2'

# list1 = list(map(int, data1.split(" ")))
# list2 = list(map(int, data2.split(" ")))

# new_list1 = []
# for i in range(list1[0], list1[2] + 1) :
#     for j in range(list1[1], list1[3] + 1) :
#         new_list1.append((i,j))

# new_list2 = []
# for i in range(list2[0], list2[2] + 1) :
#     for j in range(list2[1], list2[3] + 1) :
#         new_list2.append((i,j))

# print(set(new_list1) & set(new_list2))



test_case = int(input())

for t in range(test_case) :
    area = int(input())
    lists = []*area
    new_lists = []*area
    for i in range(area) :
        lists[i] = list(map(int, input().split(' ')))
        for i in range(lists[i][0], lists[i][2] + 1) :
            for j in range(lists[i][1], lists[i][3] + 1) :
                new_lists[i].append((i, j))
        print(new_lists[i])
                
    