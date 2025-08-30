total = 0
score = 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade != "P":
        total += float(credit)
        if grade == "A+":
            score += float(credit) * 4.5
        elif grade == "A0":
            score += float(credit) * 4.0
        elif grade == "B+":
            score += float(credit) * 3.5
        elif grade == "B0":
            score += float(credit) * 3.0
        elif grade == "C+":
            score += float(credit) * 2.5
        elif grade == "C0":
            score += float(credit) * 2.0
        elif grade == "D+":
            score += float(credit) * 1.5
        elif grade == "D0":
            score += float(credit) * 1.0
        elif grade == "F":
            score += float(credit) * 0.0
answer = score / total
print("{:.6f}".format(answer))