
def part2():
    b = input("Enter your choice (ice-cream / cookies / candies):")
    dt = {
        'ice-cream': "Remember to wash your hands",
        'cookies': "Can you share with your friends?",
        'candies': "Don’t eat too much."
    }
    if b in dt:
        print(dt[b])
        return
    else:
        print("Invalid Choice.")
        part2()

while True:
    a = input("Do you want some snacks? (yes/no)")
    if a == 'no':
        print("Good! Let’s play games instead.")
        break
    elif a == 'yes':
        part2()
    else:
        print("Please enter yes or no.")
        continue
