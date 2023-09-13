if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
    findscore = [x[1] for x in list]   # it will only take this score(int)
    sortscore = sorted(set(findscore))  # sorting this int
    findname = sorted([y[0] for y in list if(sortscore[1] == y[1])])
    for z in findname:
        print(z)