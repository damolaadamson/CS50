# A Python program that implements a greedy algorithm and asks the user how much change is owed
# before printing the minimum number of coins with which that change can be made.

while True:
    dollars = float(input("Change owed: "))
    if dollars >= 0:
        break

cents = (dollars * 100)
coins = 0

for i in [25, 10, 5, 1]:
    coins += cents // i
    cents %= i

coins = int(coins)
print(f"Coins: {coins}")
