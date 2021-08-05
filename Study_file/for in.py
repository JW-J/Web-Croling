days = ("Mon", "Tue", "Wed", "Thu", "Fri")

print(type(days))

for day in days:
    if day == "WEd":
        break
    else:
        print(day)

# is를 ==으로 바꿔주면 된다.
# 오류가 발생하는 이유는, ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(포인터)를 비교하기 때문이다.
# is 연산자는 되도록이면 None, True, False 등을 비교할 때 사용하도록 하자.

for name in "jungjoowon":
    print(name)

# String도 이론적으로는 하나의 배열이다.