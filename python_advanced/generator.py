#generators will will not save all data it will only save what we need
def sai (n:list):
    for i in range(n):
        yield i   #yeild is used in generator and it will print one value at a time

if __name__ == '__main__':
    kiran = sai(8)
    print(next(kiran)) #print one at a time
    print(next(kiran))
    print(next(kiran))
    print(next(kiran))
    print(next(kiran))



print("_____another program")
print("\n")

print("2nd program")
def hay (n:list):
    for i in range(n):
        yield i   #yeild is used in generator and it will print one value at a time

if __name__ == '__main__':
    a = hay(10**100)

    list_a: list[int] =[]
    for number in a:  #
        list_a.append(number)  # .append()is used to store the values or data in a single line
        if number == 20:
            break

    print(list_a)
    print(next(a))  #printing the next number

    list_b: list[int] = []
    for number in a:  #now we are printing from the end of abouve loop(printing from22)
        list_b.append(number)  # .append()is used to store the values or data in a single line
        if number == 40:
            break

    print(list_b)


print("2nd program can write in this way")
if __name__ == '__main__':       #we can write the same program in less code by this way
    sai = (i for i in range(10**100))

    print(next(sai))
    print(next(sai))
    print(next(sai))
    print(next(sai))
    print(next(sai))
