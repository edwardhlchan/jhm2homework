# Basic if structure
a = input("Do you want some snacks? (yes/no)\n")
if a == 'no':
    print("Good! Let’s play games instead.")
elif a == 'yes':
    b = input("Enter your choice (ice-cream / cookies / candies):\n")
    if b == 'ice-cream':
        print("Remember to wash your hands")
    elif b == 'cookies':
        print("Can you share with your friends?")
    elif b == 'candies':
        print("Don’t eat too much.")
    # elif b == "candycookiechocolate":
    #     print("DANGO")
