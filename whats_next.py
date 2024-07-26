def AP(x):
    a, b, c = x
    return c + (c - b)

def GP(x):
    a, b, c = x
    return c * (c // b)


def main():
    values = []
    answers = []
    while 1:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        values.append((a, b, c))
        if b - a == c - b:
            answers.append(("AP", AP((a, b, c))))
        else:
            answers.append(("GP", GP((a, b, c))))
    for i in answers:
        print(i[0], i[1])

main()