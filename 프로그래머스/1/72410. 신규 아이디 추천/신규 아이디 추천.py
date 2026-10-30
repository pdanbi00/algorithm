def solution(new_id):
    # 1. 대문자 -> 소문자
    new_id = new_id.lower()
    
    # 2. 소문자, '-'', '_', '.' 만 가능
    dic = ["-", "_", "."]
    check = []
    for i in range(len(new_id)):
        if new_id[i] not in dic:
            if new_id[i].isalpha() or new_id[i].isdigit():
                continue
            else:
                check.append(new_id[i])
                
    for j in range(len(check)):
        new_id = new_id.replace(check[j], "")
        
    # 3. "." 두 번 이상 등장
    while '..' in new_id:
        new_id = new_id.replace("..",".")
        
    # 4. "." 처음 or 끝에 있으면 제거
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
            
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # 5. 빈 문자열이면 a       
    if len(new_id) == 0:
        new_id = 'a'
    # 6. id 길이가 16이상이면 뒷 부분 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
            
    # 7. id 길이가 2자 이하면 마지막 문자를 길이가 3이 될때까지 붙임
    if len(new_id) <= 2:
        while True:
            if len(new_id) == 3:
                break
            else:
                last_a = new_id[-1]
                new_id = new_id + last_a
    
    return new_id