# 해당 문제는 SW Expert Academy의 문제를 응용한 것입니다.
# 임의 복제/배포를 금지합니다.

T = int(input())
for TC in range(1, T+1):
    arr = list()
    N, M = map(int,input().split())

    for i in range (N):#가로
        string = str(input())
        arr.append(string)
        for j in range(0,N-M+1):
            end = M+j
            if string[j:end] == string[j:end][::-1]:
                ans = string[j:end]
    #세로
    vertArr = list()

    for j in range(0,N):
        vertStr = str()
        vert = list()
        for i in range(0,N):
            vert.append(arr[i][j])
        vertStr = ''.join(vert)
        vertArr.append(vertStr)
        for k in range(0,N-M+2):
            end = M+k
            if vertStr[k:end] == vertStr[k:end][::-1] :
                ans = vertStr[k:end]
    
    print("#%d %s" %(TC,ans))