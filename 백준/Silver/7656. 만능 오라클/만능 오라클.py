s = input()
def sol(s):
    start, end = -1, -1
    while s.find('What', end + 1) != -1:
        start = s.find('What', end + 1)
        end = s.find('?', start + 1)
        new_s = s[start:end]
        if new_s.find('.') != -1:
            end = s.find('.', start + 1)
            continue
        print('Forty-two' + new_s[4:] + '.')
sol(s)