#mas = [list(map(int, input().split())) for i in range(int(input()))]

def determ(mas):
    if len(mas) == 2:
        d = mas[0][0]*mas[1][1] - mas[0][1]*mas[1][0]
    elif len(mas) == 3:
        d = mas[0][0]*mas[1][1]*mas[2][2] + mas[2][0]*mas[0][1]*mas[1][2] + mas[1][0]*mas[2][1]*mas[0][2]\
            - mas[2][0]*mas[1][1]*mas[0][2] - mas[0][0]*mas[2][1]*mas[1][2] - mas[1][0]*mas[0][1]*mas[2][2]
    # print(d)
    return d


def minus(mas):
    for i in range(len(list(mas))):
        for j in range(len(mas)):
            mas[i][j] = mas[i][j]*(-1)

    # print(mas)
    return mas


def increase(mas, a):
    for i in range(len(list(mas))):
        for j in range(len(mas)):
            mas[i][j] = mas[i][j]*a
    return mas


def transpose(mas):
    trans_mas = [[mas[j][i] for j in range(len(mas))] for i in range(len(mas[0]))]
    return trans_mas


def discharged_matrix(mas):
    for i in range(len(list(mas))):
        for j in range(len(mas)):
            if i == j:
                mas[i][j] = 0

    # print(mas)
    return mas


def is_discharged_matrix(mas):
    counter = 0
    for i in range(len(list(mas))):
        for j in range(len(mas)):
            if mas[i][j] == 0:
                counter = counter + 1

    m = len(list(mas))
    n = len(mas)
    return (counter >
            ((m * n) // 2))

# determ(mas)
# minus(mas)

