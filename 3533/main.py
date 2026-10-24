""" HorizontalHistogram """
def main():
    """HorizontalHistogram"""
    s = input()
    order = [chr(c) for c in range(97, 123)] + [chr(c) for c in range(65, 91)]
    for ch in order:
        c = s.count(ch)
        if c:
            BARS = ""
            for i in range(1, c + 1):
                BARS += "-"
                if not i % 5 and i != c:
                    BARS += "|"
            print(ch + " : " + BARS)

main()
