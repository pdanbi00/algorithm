E, EM, M, MH, H = map(int, input().split())
answer = 0

while True:
    e_pass, m_pass, h_pass = False, False, False

    if E:
        E -= 1
        e_pass = True
    else:
        if EM:
            EM -= 1
            e_pass = True

    if M:
        M -= 1
        m_pass = True
    else:
        if EM or MH:
            if EM >= MH:
                EM -= 1
                m_pass = True
            else:
                MH -= 1
                m_pass = True

    if H:
        H -= 1
        h_pass = True
    else:
        if MH:
            MH -= 1
            h_pass = True

    if not e_pass or not m_pass or not h_pass:
        break
    answer += 1
print(answer)