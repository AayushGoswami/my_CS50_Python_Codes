def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            part = s[2:]
            if part.isalpha():
                return True
            elif part.isalnum():
                for i in range(len(part)):
                    if part[i].isdigit():
                        part = part[i:]
                        break
                if part[0] != '0':
                    if part.isdigit():
                        return True
                    else:
                        return False
    else:
        return False


main()
