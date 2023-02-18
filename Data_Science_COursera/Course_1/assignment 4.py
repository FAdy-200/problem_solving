import pandas as pd
import numpy as np

import re

import re

p1 = r"\[edit]"
p2 = r'\('
d = []
with open("university_towns.txt", "r",encoding="UTF-8") as ut:
    for i in ut.readlines():
        gp1 = re.search(p1, i)
        gp2 = re.search(p2, i)
        if re.search(p1, i):
            z = i[:gp1.span()[0]]
        elif gp2:
            d.append([z, i[:gp2.span()[0] - 1]])
        else:
            g = [z, i[:-2]]
            d.append(g)
df = pd.DataFrame(d, columns=["State", "RegionName"])
print(df)
# g = pd.DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
#     columns=["State", "RegionName"]  )
# print(g)


