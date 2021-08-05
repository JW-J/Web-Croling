

# b의 타입이 String 이면 실행 아니면 else (현재 "10" 이기 때문에 String형식임)
def plus(a,b):
    # b타입이 integer 또는 float 형이면 실행
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

print(plus(12, 1.2))
