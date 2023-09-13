def evn_numbers(number):
    result = []
    for i in range(1, number+1):
        if i % 2 == 0:
            result.append(i)
    return result


sai = evn_numbers(10)
kiran = evn_numbers(20)

print(sai)
print(kiran)

