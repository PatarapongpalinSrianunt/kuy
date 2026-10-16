"""Laststand"""
s = input().strip()
if s.startswith('[') and s.endswith(']'):
    s = s[1:-1]

if s:
    for item in s.split(','):
        print(item.strip()[-1])
