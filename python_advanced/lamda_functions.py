 #lamda functions are normally rederred to anonoymous functions bcz of name less nature.
#A lambda function can take any number of arguments, but can only have one expression


def saikiran(a:float)->float:
    return a**2

sk = lambda a: a**2

print(saikiran(4))
print(sk(5))


#Other program that prints the even number by the given number

print("\n Another program")
numbers: list[int] = [1,3,2,4,8,3,5,6,7,7,6,6,6]

even: list[int] = list(filter(lambda a:a%2 ==0,numbers))
print(even)
