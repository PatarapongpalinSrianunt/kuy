"""team"""
d1 = input().split()
n = int(d1[0])
m = int(d1[1])

if not 1 <= n <= 10 or not 1 <= m <= 20:
    print("Data Incorrect")
else:
    teams = []
    has_invalid = False
    i = 0
    while i < n:
        row = input().split()
        scores = []
        j = 0
        while j < m:
            val = int(row[j])
            if not 0 <= val <= 100:
                has_invalid = True
            scores.append(val)
            j += 1
        teams.append(scores)
        i += 1

    if has_invalid:
        print("Data Incorrect")
    else:
        total_all = 0
        i = 0
        while i < n:
            s_sum = 0
            s_max = -1
            j = 0
            while j < m:
                sc = teams[i][j]
                s_sum += sc
                if sc > s_max:
                    s_max = sc
                j += 1
            avg = s_sum / m
            total_all += s_sum
            print(f"Team {i + 1}: Average = {avg:.2f}, Max = {s_max}")
            i += 1
        print(f"Total Score of All Teams = {total_all}")
