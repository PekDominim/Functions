let1 = input("Enter first string: ")
let2 = input("Enter second string: ")
let3 = input("Enter third string: ")

listname = [let1, let2, let3]
x =  2147483647
y = ""
for i in listname:
    if len(i) < x:
        x = len(i)
        y = i

print(y)
