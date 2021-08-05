#소수점 계산 부분 처리

def check(CheckNum1, CheckNum2, Checksum):
    # CheckNum1/2가 int 또는 float 가 아닌경우 brack
    if Checksum == "1" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "2" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "3" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "4" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "5" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "6" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    if Checksum == "7" :
        a = "%g" %CheckNum1
        b = "%g" %CheckNum2
        c = "%g" %(CheckNum1+CheckNum2)
        return print (f"{a} + {b} = {c}")

    else:
        print("연산자 번호를 제대로 입력하세요..")
# 값을 받는 구간

re=str(input("연산자 선택해주세요. [1-7] : "))
one=float(input("첫번째:"))
twe=float(input("두번째:"))