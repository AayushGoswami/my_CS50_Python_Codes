def main():
   print(fuel("Fraction: "))


def fuel(prompt):
    while True:
        try:
            value = (input(prompt)).strip()
            n,d = value.split("/")
            value = int(n)/int(d)*100
            if 0 <= value <= 1:
                return ("E")
            elif 1 < value < 99:
                return (f"{value: .0f}%")
            elif 99 <= value <= 100:
                return ("F")
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass


main()
