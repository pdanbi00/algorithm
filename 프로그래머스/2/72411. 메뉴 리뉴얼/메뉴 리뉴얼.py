info = dict()
def solution(orders, course):
    answer = []
    orders_list = []
    for order in orders:
        arr = list(order)
        arr.sort()
        orders_list.append(arr)

    
    for cnt in course:
        # info = dict()
        max_cnt = 0
        for order in orders_list:
            dfs(0, "", order, cnt)
        
        if info:
            max_value = max(info.values())
            if max_value > 1:
                for k, v in info.items():
                    if v == max_value:
                        answer.append(k)
        info.clear()      
    answer.sort()
    return answer

def dfs(depth, menu, chars, total):
    # print(depth, menu, chars, total)
    if total == len(menu):
        if menu in info:
            info[menu] += 1
        else:
            info[menu] = 1
        return
    
    if depth >= len(chars):
        return
    
    dfs(depth + 1, menu + chars[depth], chars, total)
    dfs(depth + 1, menu, chars, total)