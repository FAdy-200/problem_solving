time = input().split(":")
pfix = time[-1][2:]
time[-1] = time[-1][:2]
if pfix == "AM" and time[0] == "12":
    time[0] = "00"
elif pfix == "PM" and time[0] != "12":
    time[0] = str(int(time[0])+12)
print(":".join(time))
