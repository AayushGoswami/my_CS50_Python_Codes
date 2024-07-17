def main():
    interpret(input("Expression: ").strip())

def interpret(num):
    x,y,z = num.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        print(f"{x+z: .1f}")
    elif y == "-":
        print(f"{x-z: .1f}")
    elif y == "*":
        print(f"{x*z: .1f}")
    elif y == "/":
        print(f"{x/z: .1f}")


main()
