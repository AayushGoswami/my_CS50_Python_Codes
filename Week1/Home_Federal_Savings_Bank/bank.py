def main():
    greeting(input("Greeting: ").strip().lower())

def greeting(string):
    if string.startswith("h"):
        if string.startswith("hello"):
            print("$0")
        else:
            print("$20")
    else:
        print("$100")


main()
