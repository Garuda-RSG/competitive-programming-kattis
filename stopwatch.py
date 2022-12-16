button_presses = int(input())

times = [int(input()) for _ in range(button_presses)]

if button_presses % 2 == 0:
    time_on_watch = 0
    for i in range(0, button_presses, 2):
        time_on_watch += times[i+1] - times[i]
    print(time_on_watch)
else:
    print("still running")