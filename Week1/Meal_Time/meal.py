def main():
    #Takes the input from the user and passes it to the convert() fucntion
    times = convert(input("What time is it? ").strip().lower())

    #Checking for the time conditions

    if 7 <= times <= 8:
        print("breakfast time")
    elif 12 <= times <= 13:
        print("lunch time")
    elif 18 <= times <= 19:
        print("dinner time")

def convert(time):
    # if the input of time is in ##:## am or ##:## pm format
    if time.endswith("am") or time.endswith("pm"):
        h_m, p_a = time.split(" ")
        h, m = h_m.split(":")
        if p_a == "pm" and int(h) != 12:
            h = int(h) + 12
        if p_a == "am" and int(h) == 12:
            h = 0

    # if the input of time is in the ##:## format
    else:
        h, m = time.split(":")
    h = float(h) + (float(m)/60)

    return h


if __name__ == "__main__":
    main()
