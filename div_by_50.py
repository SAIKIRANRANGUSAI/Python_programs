def sai(num: float):

    if num < 50:
        print("please enter a valid number")
    elif num % 50 == 0:
        print("its divisible by 50")
    else:
        print("the number is not divisible by 50")


num = float(input("enter a number:"))
sai(num)


