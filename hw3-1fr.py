n = int(input("Input Addition Table Size smaller 10: "))
print("Addition Table")
print("-" * 55)
expect_longest = len(str(n + n)) + 1
stra = f""
for i in range(n*n):
    stra += f"{i//n + 1} + {i%n + 1} = {(i//n+1) + (i%n+1)}" + " "*(expect_longest - len(str((i//n+1) + (i%n+1))))
    if i % n == n - 1:
        print(stra)
        stra = ""

print("-" * 55)