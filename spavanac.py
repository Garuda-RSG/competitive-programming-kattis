hours, minutes = [int(time) for time in input().split()]

if hours == 0:
    hours = 24

total_minutes = (60 * hours) + minutes - 45
out_hours = total_minutes // 60
out_minutes = total_minutes % 60

print(f"{out_hours} {out_minutes}")