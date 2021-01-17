# String

# 문자표현
# 컴퓨터에서의 문자표현
# 글자 A를 메모리에 저장하는 방법
# 1) 메모리는 숫자만을 저장할 수 있기 때문에 A라는 글자의 모양 그대로 비트맵으로 저장하는 방법
# 2) 각 문자에 대해서 대응되는 숫자를 정해 놓고 이것을 메모리에 저장하는 방법
# 후자를 코드 체계라고 함, 영어는 대소문자 합쳐서 52개이므로, 6비트(64가지)면 모두 표현할 수 있음
# ex) 000000 => 'a', 000001 => 'b'

# 이러한 코드 체계를 표준화 한 것이, ASCII(American Standard Code for Information Interchange)
# 아스키(ASCII) 코드는, 7비트 인코딩으로 128문자를 표현하며 33개의 출력 불가능한 제어 문자들과 공백을 비롯한 95개의 출력 가능한 문자들로 이루어져 있음
# 확장 아스키 코드는 표준 문자 이외의 악센트 문자, 도형문자, 특수 문자, 특수 기호 등 부가적인 문자를 128개 추가할 수 있게 하는 부호
# 1바이트(8비트)를 모두 사용함으로써 추가적인 문자를 표현할 수 있음
# 다만, 확장부호는 표준 아스키와 다르게 서로 다른 프로그램이나 컴퓨터 사이에 교화되지 못함, 해독할 수 있도록 설계되어 있어야만 올바로 해독할 수 있음

# 유니코드 : 다국어 처리를 위한 표준
# 대부분의 컴퓨터는 문자를 읽고 쓰는데 아스키 코드 형식을 사용했었음
# 컴퓨터가 발전하면서 각 국가들은 자국의 문자를 표현하기 위하여 코드 체계를 만들어서 사용
# 인터넷이 전 세계로 발전하면서 국가 간에 정보를 주고 받을 때 해독 문제 발생
# 다국어 처리를 위한 표준이 필요해짐, 이를 유니코드라고 함
# 유니코드 인코딩(UTF : Unicode Transformation Format)
# UTF-8(in web) : min 8bit, max 32bit
# UTF-16(in windows, Java) : min 16bit, max 32bit
# UTF-32(in unix) : min, max 32bit
# 파이썬의 기본 인코딩은 UTF-8

# 문자열의 분류
# 문자열 : 1) Fiexed Lenght(고정길이), 2) Variable Length(가변길이)-(Length controlled(Java 언어), Delimited(C언어))
# 파이썬에서의 문자열 처리는 Java나 C언어에 비해 간편
# 문자열은 시퀀스 자료형으로 분류되고, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산들을 사용할 수 있음
# 문자열은 튜플과 같이 요소값을 변경 할 수 없음


## 패턴매칭
# 문자열 교체하기
# 문자열 내에서 '1, 2'라는 문자열을 'one, two'라는 문자열로 변경하는 경우
# abc, 1, 2 ABC => ABC를 복사
# abc one, two로 교체
# ABC를 복사해서 붙여넣기

# 고지식한 알고리즘(Brute Force)
# 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작
# 시간 복잡도 : O(MN)

text = 'This is a book'
pattern = "is"
M = len(text)
N = len(pattern)

def BruteForce(text, pattern):
    i = 0
    j = 0
    while i < M and j < N :
        if text[i] != pattern[j] :
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == N : 
        return i - N
    else : 
        return -1

# KMP 알고리즘
# 불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
# 시간 복잡도 : O(M+N)
# ex) 
# abcdabcd
# abcdabce의 경우,  
# abcdabcd
# 0000abcdabce를 비교
# 돌아갈 곳을 지정해놓으면 됨

# 보이어-무어 알고리즘
# 오른쪽에서 왼쪽으로 비교
# 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우, 패턴의 길이만큼 오른쪽으로 이동
# ex)
# abcdbwater
# water
# 00000water

# 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재할 경우, 해당하는 문자의 시작 위치만 큼 이동
# ex)
# a pattern matching algorithm
# rithm
# m = 0, h = 1, t = 2, i = 3, r = 4, 다른 문자 = 5 스킵
# 오른쪽 끝 문자 m, t 불일치 -> 그러나 t는 패턴내에 존재, 2만큼 이동
# a pattern matching algorithm
# 00rithm
# 오른쪽 끝 문자 m, e 불일치 -> e는 패턴내에 미존재 5만큼 이동
# a pattern matching algorithm
# 0000000rithm
# 반복
# a pattern matching algorithm
# 000000000000rithm
# a pattern matching algorithm
# 00000000000000000rithm
# a pattern matching algorithm
# 0000000000000000000000rithm
# 오른쪽 끝 문자 m, h 불일치 -> 그러나 h는 패턴내에 존재, 1만큼 이동
# a pattern matching algorithm
# 00000000000000000000000rithm

