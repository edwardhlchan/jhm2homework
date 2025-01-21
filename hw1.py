num1 = float(input("Enter a price: "))
num2 = float(input("Enter another price: "))


res = { # list data
    1 : [" first", "", "is", "larger than the second one."],
    0: ["", "s", "are", "the same."],
    -1: [" first", "", "is", "smaller than the second one."]    
}

res_ = (num1 > num2) - (num1 < num2) #boolean math, 1 for true, 0 for false
ls = res[res_] # list assignment
print("The%s price%s %s %s" % (ls[0], ls[1], ls[2], ls[3])) # string substitution
