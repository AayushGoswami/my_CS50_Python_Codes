# This code is totally writte by my in VS Code in my personal laptop during the time when cs50.dev was having a partial outage today.

def main():
    calories(input("Item: ").strip().lower())


def calories(item):
    cal = {
            "apple":"130",
            "avocado":"50",
            "banana":"110",
            "cantaloupe":"50",
            "grapefruit":"60",
            "grapes":"90",
            "honeydew melon":"50",
            "kiwifruit":"90",
            "lemon":"15",
            "lime":"20",
            "nectarine":"60",
            "orange":"80",
            "peach":"60",
            "pear":"100",
            "pineapple":"50",
            "plum":"70",
            "strawberries":"50",
            "sweet cherries":"100",
            "tangerine":"50",
            "watermelon":"50",
            }
    if item in cal:
        print(f"Calories: {cal[item]}")

main()
