def say_hello(name, age):
    return f"hello {name} you are {age} years old"

hello = say_hello("jwjung", 29)
print(hello)


# 위 방법은 인수를 전부 알아야하지만 아래 방법은 인수의 이름으로 넣어줄 수있다.
def say_hello2(name, age):
    return " hello " + name + " you are " + age + " years old "

hello2 = say_hello2(name="jwjung", age="29")
print(hello2)


# Beat 방법
def say_hello3(name, age, are_from, fav_food):
    return f"hello {name} you are {age} you are from {are_from} you like {fav_food}"

hello3 = say_hello3("jwjung", "29", are_from="korea", fav_food="banana" )

# SyntaxError 발생합니다. Keyworded Arguments 문법 적으로 에러가 발생
# 키워드 어규먼트를 뒤에서 쓰고 앞에 고정매개변수를 넣어주면 가능함.
#hello3 = say_hello3(are_from="korea", fav_food="banana", "jwjung", "29")
print(hello3)