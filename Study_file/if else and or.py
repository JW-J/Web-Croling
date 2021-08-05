def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you are Drink")
    # 둘중 하나만 포함되도 실행이됨.
    elif age == 18 or age == 19:
        print(" you are new to this~!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(18)
