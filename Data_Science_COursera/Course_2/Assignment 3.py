import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import pandas as pd
# %matplotlib notebook #Comment this line if not using jupyter


def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return h


# Use the following data for this assignment:


np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])

t = df.transpose()
g = t.describe()
g.loc["mean1"] = g.loc["mean"]
for i in g.columns:
    g.loc["95%", i] = mean_confidence_interval(t[i])
    for j in range(1, 10):
        g.loc["{}0%m".format(j), i] = mean_confidence_interval(t[i], confidence=j / 10)

g = g.iloc[-11:]
cs = ['FBE2DD', 'DFC8D3', 'C3AFCA', 'A796C1', '8B7DB8', '6F64AF', '534BA6', '37329D', '1B1994', "00008B"]
cb = ["FBE2DD", "EEC8C4", 'E2AFAB', 'D59693', 'C97D7A', 'BC6462', 'B04B49', 'A33231', '971918', '8B0000']


def co(yn):
    sol = []
    for i in range(4):
        c = yn >= g.iloc[0, i]
        s = (i, 1, "S")
        b = (i, 1, "B")
        for j in range(2, 11):
            if c and g.iloc[0, i] + g.iloc[j, i] <= yn:
                s = (i, j, 'S')
            elif (not c) and (g.iloc[0, i] - g.iloc[j, i]) >= yn:
                b = (i, j, 'B')
        if c:
            sol.append(s)
        else:
            sol.append(b)
    return sol



fig = plt.figure()

bars = plt.bar(g.columns, g.loc["mean1"].astype("float"), yerr=g.loc["95%"], capsize=8)
plt.xticks(g.columns, (g.columns.astype("str")))

kk = 0
plt.title("No Y value requested yet please click on the graph")

def on_press(event):
    global kk, gh
    yo = event.ydata
    if kk != 0:
        gh.remove()
    plt.title("Y value requested = {}".format(yo))
    gh = plt.axhline(y=yo, color="orange")
    kk = 1
    sl = co(yo)
    for i in sl:
        if i[2] == "S":
            bars[i[0]].set_color("#" + cs[i[1] - 1])
        else:
            bars[i[0]].set_color("#" + cb[i[1] - 1])
    plt.show()


cid = fig.canvas.mpl_connect('button_press_event', on_press)
plt.show()
