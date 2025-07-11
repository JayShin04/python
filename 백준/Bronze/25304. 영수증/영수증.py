totalAmountInRecipe = int(input())
KindOfBoughtStuff = int(input())
totalPrice = 0
for i in range(KindOfBoughtStuff):
  price, amount = map(int, input().split())
  tempTotalPrice = price * amount
  totalPrice += tempTotalPrice
if totalAmountInRecipe == totalPrice:
  print("Yes")
else:
  print("No")