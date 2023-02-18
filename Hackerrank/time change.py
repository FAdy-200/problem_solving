x = input().split(":")
if x[2][2:] == "PM" and x[0] != "12":
    x[0] = str(int(x[0])+12)
elif x[2][2:] == "AM" and x[0] == "12":
    x[0] = "00"
x[2] = x[2][:2]
print(":".join(x))
