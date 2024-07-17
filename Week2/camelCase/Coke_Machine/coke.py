def main():
    price = 50
    while price > 0:
        print("Amount Due:", price)
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            price -= coin
    print("Change Owed:", abs(price))

main()
