from datetime import datetime

def solution(age):
    y = datetime.today().year
    answer = y - age
    return answer