""" SqFree """
def main():
    """SqFree"""
    n = int(input())
    ans = 0
    for a in range(1, n + 1):
        free = True
        b = 2
        while b * b <= a:
            if not a % (b * b):
                free = False
                break
            b += 1
        if free:
            ans += 1
    print(ans)

main()
