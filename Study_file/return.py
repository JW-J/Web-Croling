def p_plus(a,b):
    print(a+b)

def r_plus(a,b):
    return a+b


p_result = p_plus(2,3)
r_result = r_plus(2,3)

# p_result 의 경우 말그대로 print만 한것
# r_result 는 r_result = 5 라고 한것
# 즉 반환했기 때문에 r_result에 5값이 있는거고, p_result는 값이 없는거고,
print(p_result, r_result)
# return 시 펑션은 그대로 종료되며 그 아래 명령어는 실행이 안됨.


# 아래 예제는 그 result를 받아서 다시 계산이 가능하네
def r_plus(a,b):
    return a+b

result = r_plus(2,3)
print(result)

c=result+4
print(c)