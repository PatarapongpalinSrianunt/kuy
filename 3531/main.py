""" MissingNumber """
def main():
    """MissingNumber"""
    n = int(input())
    given_numbers = set()
    while True:
        num = int(input())
        if not num:
            break
        given_numbers.add(num)
    missing_numbers = []
    for i in range(1, n + 1):
        if i not in given_numbers:
            missing_numbers.append(i)
    for num in missing_numbers:
        print(num)

main()
