"""BusStop I"""
p = int(input().strip())
n = int(input().strip())

boarding_passengers = {}
for _ in range(n):
    tokens = list(map(int, input().strip().split()))
    stop_id = tokens[0]
    destinations = tokens[1:]
    boarding_passengers[stop_id] = destinations

bus = []  # รายชื่อปลายทางของผู้โดยสารที่อยู่บนรถปัจจุบัน
successful_get_offs = 0  # ตัวแปรนับจำนวนผู้โดยสารที่ได้ลงตามป้าย

for current_stop in range(1, n + 1):
    arrived_count = bus.count(current_stop)
    successful_get_offs += arrived_count
    bus = [d for d in bus if d != current_stop]

    waiting = boarding_passengers.get(current_stop, [])
    for dest in waiting:
        if dest > current_stop and len(bus) < p:
            bus.append(dest)

print(successful_get_offs)
