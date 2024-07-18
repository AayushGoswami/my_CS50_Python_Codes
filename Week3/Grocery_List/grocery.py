def main():
    grocery()

def grocery():
    items = {}
    while True:
        try:
            item = (input().upper().strip())
            if item.isnumeric():
                continue
            else:
                items[item] = items.get(item, 0) + 1
        except EOFError:
            print()
            break
    items = sorted(items.items(), key=lambda x: x[0])
    for item, count in items:
        print(f"{count} {item}")


main()
