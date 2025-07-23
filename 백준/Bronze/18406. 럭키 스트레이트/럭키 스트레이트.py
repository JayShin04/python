N = input()
half = len(N) // 2

halfFront = [int(i) for i in N[:half]] 
halfBack = [int(i) for i in N[half:]]
if sum(halfFront) == sum(halfBack):
    print("LUCKY")
else:
    print("READY")