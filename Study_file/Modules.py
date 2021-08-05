# 모듈 전체를 가져와 사용

#  math에 특정 함수만 가져와 ceil, fsum만 사용
from math import ceil, fsum

# 값을 올림한다.
print(ceil(1.2))

# 값의 합계를 반환한다.
print(fsum([1.2,3,4,5]))

# math의 모듈에 fsum명칭을 Total_Sum 으로 변경한다.
from math import fsum as Total_Sum
print(Total_Sum([1,2,3,4]))

# calculator의 특정 함수만 가져와서 사용한다.
from calculator import plus, minus
print(plus(1,2))
print(minus(1,2))

# print 는 무제한의 매개 변수를 받을 수 있다.
# 이는 이후 Django 를 사용할때 필수인 개념으로 후반에 나옴.
print(plus(1,2), minus(1,2), 13, "dsfsdfdsf")





