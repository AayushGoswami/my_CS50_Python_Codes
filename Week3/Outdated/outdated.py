def main():
    dated("Date: ")

def dated(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input(prompt).strip().capitalize()
            if "/" in date:
                mm, dd, yyyy = date.split("/")
                if (1 <= int(mm) <=12) and (1 <= int(dd) <= 31) and (int(yyyy) > 0):
                    print(f"{int(yyyy):04}-{int(mm):02}-{int(dd):02}")
                    break
                else:
                    pass
            elif (" " and ",") in date:
                month, day, year = date.split(" ")
                dd, yyyy = int(day.strip(",")), int(year)
                if (month in months) and (1<=dd<=31) and (yyyy>0):
                    mm  = months.index(month) + 1
                    print(f"{int(yyyy):04}-{int(mm):02}-{int(dd):02}")
                    break
                else:
                    pass
            else:
                pass
        except ValueError:
            pass
        except EOFError:
            print()
            break

main()
