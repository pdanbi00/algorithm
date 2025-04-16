dots = list(map(int, input().split()))

first = dots[:2]
second = dots[2:4]
third = dots[4:6]
fourth = dots[6:]

if (first[0] - second[0]) == 0 or (third[0] - fourth[0]) == 0:
    # x = 3과 같은 직선 그래프랑 만날 경우
    if (first[0] - second[0]) == 0 and (third[0] - fourth[0]) != 0:
        degree_2 = (fourth[1] - third[1]) / (fourth[0] - third[0])
        b_2 = third[1] - (degree_2 * third[0])
        x = first[0]
        y = degree_2 * x + b_2
        if min(third[0], fourth[0]) < x < max(third[0], fourth[0]) and min(first[1], second[1]) < y < max(first[1], second[1]):
            print(1)
        else:
            print(0)

    elif (first[0] - second[0]) != 0 and (third[0] - fourth[0]) == 0:
        degree_1 = (second[1] - first[1]) / (second[0] - first[0])
        b_1 = first[1] - (degree_1 * first[0])
        x = third[0]
        y = degree_1 * x + b_1
        if min(first[0], second[0]) < x < max(first[0], second[0]) and min(third[1], fourth[1]) < y < max(third[1], fourth[1]):
            print(1)
        else:
            print(0)
    else:
        print(0)

else:
    degree_1 = (second[1] - first[1]) / (second[0] - first[0])
    b_1 = first[1] - (degree_1 * first[0])

    degree_2 = (fourth[1] - third[1]) / (fourth[0] - third[0])
    b_2 = third[1] - (degree_2 * third[0])

    if degree_1 == degree_2:
        print(0)
    else:
        x = (b_2 - b_1) / (degree_1 - degree_2)
        y = (degree_1 * x) + b_1

        if (min(first[0], second[0]) < x < max(first[0], second[0])) and (min(third[0], fourth[0]) < x < max(third[0], fourth[0])) and (min(first[1], second[1]) < y < max(first[1], second[1])) and (min(third[1], fourth[1]) < y < max(third[1], fourth[1])):
            print(1)
        else:
            print(0)