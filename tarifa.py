X = int(input())
N = int(input())
P = [int(input()) for months in range(N)]

# megabytes Pero will have available in the N+1
# month of using the plan

mb_available = (X * (N + 1)) - sum(P)
print(mb_available)