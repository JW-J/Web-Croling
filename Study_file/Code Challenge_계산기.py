def check(CheckNum1, CheckNum2, Checksum):
    if Checksum == "+" :
        a = float(CheckNum1)
        b = float(CheckNum2)
        c = a+b
        return print(f"{a} + {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "-" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a-b
        return print(f"{a} - {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "*" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a*b
        return print(f"{a} * {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "/" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a/b
        return print(f"{a} / {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "**" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a**b
        return print(f"{a} ** {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "//" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a//b
        return print(f"{a} // {b} = {c}")

    elif CheckNum1.isnumeric() and CheckNum2.isnumeric() and Checksum == "%" :
        a = int(CheckNum1)
        b = int(CheckNum2)
        c = a/b
        return print(f"{a} % {b} = {c}")
    else :
        print("Error")

# 값을 받는 구간

re=input("연산자 선택해주세요")
one=input("첫번째:")
twe=input("두번째:")

check(one,twe,re)