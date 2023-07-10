money = int(input("How much money are you investing? "))
profit = int(input("How much is the profit (In %)? ")) / 100
years = int(input("For how many years are you investing? "))

for i in range(years):
    money += (money * profit)

print(str(money) + "€" )