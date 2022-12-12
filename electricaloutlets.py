test_cases = int(input())
for case in range(test_cases):
    strips = [int(strip) for strip in input().split()[1:]]
    print(sum(strips) - len(strips) + 1)