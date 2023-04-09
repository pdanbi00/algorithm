while True:
    sentances = input()
    if sentances == '#':
        break
    else:
        sentances = sentances.upper()
        cnt = 0
        for s in sentances:
            if s == 'A' or s == 'E' or s == 'I' or s == 'O' or s == 'U':
                cnt += 1

        print(cnt)