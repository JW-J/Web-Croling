def plus(a,b):
    print(a + b)

def minus(a, b=0):
    print(a-b)

plus(1,2)
minus(7)


# 사용자에게 값을 받아 던질때 String 형으로 들어간다.
# 그렇기 때문에 던질때 형변환을 해준 후 넣어줘야 한다
# function 안에서는 연산이 안먹는듯?
def plus_test(a,b=0):
    print("여기서부터 plus_test시작")
    print(a+b)
    print(1+2)

plus_test(int(input('')), int(input('')))




