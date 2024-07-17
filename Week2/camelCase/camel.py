def main():
    # Take the camelCase string input from the user
    camel_snake(input("camelCase: ").strip())
# camelCase to snake_case converter
def camel_snake(camel):
    for char in camel:
        # change the uppercaase character in the camelCase string to _snake case character
        if char.isupper():
            char = char.lower()
            print(f"_{char}", end = '')
        # else continue as it is
        else:
            print(char, end = '')
    print()

main()
