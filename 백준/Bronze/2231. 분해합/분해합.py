# N이 있을때 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미
# M의 분해합이 N인 경우, M을 N의 생성자라고 한다
# 245의 분해합은 256이 되며
# 256의 생성자는 245라고 말할 수 있다.

#자연수 N이 주어졌을때, N의 가장 작은 생성자를 구해내는 프로그램 작성하기

# 216을 입력하면 #216의 생성자중 가장 작은 수인 198을 출력

N = input()
lengthOfN = len(N)
N = int(N)
startNumber = max(0, N - (9 * lengthOfN))
result = -1
while True:
    if startNumber > N:
        break
    numberList = [int(startNumber)]
    for i in str(startNumber):
        numberList.append(int(i))
    if sum(numberList) == N:
        result = numberList[0]
        break
    startNumber = int(startNumber) + 1
if result == -1:
    print(0)
else:
    print(result)


