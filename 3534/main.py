""" Filter """
import ast
def main():
    """Filter"""
    d = ast.literal_eval(input())
    thr = float(input())
    out = []
    for k in sorted(d):
        if d[k] >= thr:
            out.append(f"{k}\t{d[k]:.2f}")
    if out:
        print("\n".join(out))
    else:
        print("Nope")

main()
