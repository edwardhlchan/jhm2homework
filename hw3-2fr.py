n = int(input("Input Addition Table Size smaller 10: "))
print("Addition Table")
print("-" * 55)
expect_longest = len(str(n + n)) + 1
for i in range(1, n+1):#loop 1
    for j in range(1, n+1): #loop 2
        print("%d + %d = %d" % (i, j, i+j), end=(" "*(((n+n)//10+1)-(i+j)//10))) #print the result
    #    print("%d + %d = %d" % (i, j, i+j), end=(" "*(expect_longest - len(str(i+j))) # Versatile version

    print()
print("-" * 55)