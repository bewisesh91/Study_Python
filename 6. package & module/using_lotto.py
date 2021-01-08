# lotto module 사용해보기

# 로또 번호의 시작 번호를 입력하세요 (기본값 : 1)
# 로또 번호의 끝 번호를 입력하세요 (기본값 : 45)
# 로또 공의 개수를 입력하세요 (기본값 : 6)

import lotto

start = lotto.input_start()
end = lotto.input_end()
count = lotto.input_count()

lotto.print_lotto(start, end, count)