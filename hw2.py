
def part2():
    b = input("Enter your choice (ice-cream / cookies / candies):")
    dt = {
        'ice-cream': "Remember to wash your hands",
        'cookies': "Can you share with your friends?",
        'candies': "Don’t eat too much."
    }
    print(dt.get(b, "Invalid choice"))

a = input("Do you want some snacks? (yes/no)")
if a == 'no':
    print("Good! Let’s play games instead.")
elif a == 'yes':
    part2()


    # elif b == "candycookiechocolate":
    #     print("DANGO")