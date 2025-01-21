ls = []
for i in range(1,5):
    while True: # go into checking loop
        n = float(input(f"Input the height of a student {i} in cm: "))
        if n < 0:
            print("Height must be positive.")
        elif n > 200:
            print("Height is greater than 200cm.")
        else:
            ls.append(n)
            break
print("End of input.")
print(f"The average height of these students is {sum(ls)/len(ls):.2f} cm.") # calc avg, print 2 decimal
print(f"The maximum height of these students is {max(ls):.2f} cm.") # calc max, print 2 decimal

# sir this code is basically self explantory i cant explain it more than this