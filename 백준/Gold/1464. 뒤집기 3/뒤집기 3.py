'''
문자열을 reverse 하는건 0번 인덱스부터 i번 인덱스까지 reverse하는거임
그러니깐 사전순으로 앞선 문자를 만나면 영향을 덜 받는 뒷 쪽 인덱스로 밀어넣고 제일 마지막에 뒤집으면 됨

i번째 문자를 i+1번째 문자로 보내는 방법은 한가지
i번째 문자까지 뒤집고 다시 i+1번째 문자까지 뒤집는 방법
1.초기상태
a1 a2 a3 a4...ak ak+1
2. i번째 문자까지 뒤집기
ak ak-1 ... a4 a3 a2 a1 ak+1
3. i+1번째 문자까지 뒤집기
ak+1 a1 a2 a3 a4 ... ak-1 ak

근데 이건 ak < ak+1일때만 해야 됨.

근데 생각해보면
ak >= ak+1이면
a1 a2 a3 a4 ... ak-1 ak ak+1이 됨

즉, 현재까지 구한 문자열을 s라 하고, 현재 문자가 k라고 했을 때
sk-1 < ak일 경우에는 ak + s가 되고
sk-1 >= ak일 경우에는 s + ak가 됨 reverse 안해도 되긴 함.
'''

S = list(input())
N = len(S)
ascii_code = []
reverse = []

# 문자를 아스키코드로 변환
for s in S:
    ascii_code.append(ord(s))

target = ascii_code[0]
reverse.append(target)

for i in range(1, N):
    # 타겟과 현재 아스키코드 비교
    if target < ascii_code[i]:
        reverse.reverse()
        reverse.append(ascii_code[i])
        reverse.reverse()
    else:
        target = ascii_code[i]
        reverse.append(ascii_code[i])
reverse.reverse()
for i in reverse:
    print(chr(i), end="")