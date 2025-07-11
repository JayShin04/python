dice1, dice2, dice3 = map(int, input().split())
triple = 0
same = 0
price = 0
if dice1 == dice2:
  same = dice1
  if same == dice3:
    triple = same

if dice1 == dice3:
  same = dice1
  if same == dice2:
    triple = same

if dice2 == dice3:
  same = dice2
  if same == dice1:
    triple = same

if triple != 0:
  price = 10000 + triple * 1000
elif same != 0:
  price = 1000 + same * 100
else :
  biggest = dice1
  if (dice2 > biggest):
    biggest = dice2
  if (dice3 > biggest):
    biggest = dice3
  price = biggest * 100
print(price)