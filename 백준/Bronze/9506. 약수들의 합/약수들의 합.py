while True:
    N = int(input())
    if N == -1:
        break
    divisor = [ ]
    for i in range(1, N):
        if N % i == 0:
            divisor.append(i)
    sum = 0
    sumArray = [ ]
    answer = ""
    for i in divisor:
        sum += i
        sumArray.append(i)
    if sum == N:
        answer = str(N) + " = " + str(sumArray[0])
        for j in sumArray[1:]:
            answer += " + " + str(j)
        print(answer)
    else:
        print(N, "is NOT perfect.")