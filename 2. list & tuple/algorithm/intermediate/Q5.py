# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

# 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

test_case = int(input())
for t in range(test_case) :
    area = int(input())
    
    lists = []
    new_lists = []
    sets = set()
    for a in range(area) :
        lists.append([])
        lists[a] = list(map(int, input().split(' ')))
        for i in range(lists[a][0], lists[a][2] + 1) :
            for j in range(lists[a][1], lists[a][3] + 1) :
                new_lists.append((i,j))
                sets.add((i, j))
    print(f'#{t+1} {len(new_lists)-len(sets)}')