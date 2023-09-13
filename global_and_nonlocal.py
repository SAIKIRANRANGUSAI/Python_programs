def fun():
    x = 10

    def inn_fun():
        nonlocal x
        x = 20
        print("inner",x)

    inn_fun()

    print("outer",x)
fun()