import re
import csv

f = open("logs.log", "r+")
p = r"error|info"
pe = r"error"
pi = r"info"
error = dict()
per_user = dict()
username = r"\(.+\)"
ermsg = r"ERROR([ \w+]+)"
for i in f.readlines():
    if re.search(p, i.lower()):
        user = re.search(username, i).group()
        if per_user.get(user):
            if re.search(pe, i.lower()):
                err = re.search(ermsg, i).group(1).strip()
                if error.get(err):
                    error[err] += 1
                else:
                    error[err] = 1
                per_user[user][1] += 1
            else:
                per_user[user][0] += 1
        else:
            if re.search(pe, i.lower()):
                err = re.search(ermsg, i).group(1).strip()
                if error.get(err):
                    error[err] += 1
                else:
                    error[err] = 1
                per_user[user] = [0, 1]
            else:
                per_user[user] = [1, 0]
k = sorted(error.items(), key=lambda x: x[1], reverse=True)
m = sorted(per_user.items())
with open("error_message.csv", "w") as out:
    fin = ["Error, Count"] + ["{}, {}".format(i[0], i[1]) for i in k]
    out.write("\n".join(fin))
with open("user_statistics.csv", "w") as out:
    fin = ["Username, INFO, ERROR"] + ["{}, {}, {}".format(i[0][1:-1], i[1][0], i[1][1]) for i in m]
    out.write("\n".join(fin))
    # print(m)