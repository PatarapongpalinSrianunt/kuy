"""PickThemAgain"""
numbers = input().split()
numbers.reverse()
num = []
for i in numbers:
    if not int(i) % 3 or not int(i) % 5:
        num.append(i)
if num:
    for i in num:
        print(i)
else:
    print("Nope")
