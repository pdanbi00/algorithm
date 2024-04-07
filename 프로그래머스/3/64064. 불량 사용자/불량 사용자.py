from itertools import permutations
def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*':
                continue
            if users[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer_list = []
    for users in permutations(user_id, len(banned_id)):
        if not check(users, banned_id):
            continue
        else:
            user = set(users)
            if user not in answer_list:
                answer_list.append(user)
    
    return len(answer_list)