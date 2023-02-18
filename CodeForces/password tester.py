a = "abcdefghijklmnopqrstuvwxyz"
x = 0
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
y = 0
n = "0123456789"
z = 0
s = "!@#$%^&*()_+"
w = 0
password = input("Please enter your password to be checked : ")
if 6 < len(password) < 16:
    for c in password:
        if c in A:
            x = 1
        if c in a:
            y = 1
        if c in n:
            z = 1
        if c in s:
            w = 1
if (x+y+z+w) == 4:
    print("valid")
else:
    print("invalid")