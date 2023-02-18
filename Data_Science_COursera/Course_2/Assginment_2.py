import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates


def mn(df, x):
    return min(df[x])


def mx(df, x):
    return max(df[x])


def av(dff, x):
    return np.average(dff[x])


gg = pd.read_csv("temp_data.csv")
gg["Data_Value"] = (gg["Data_Value"]) / 10
gg["Date"] = gg["Date"].astype("datetime64")
gg.sort_values(by='Date', inplace=True)
gg.index = pd.to_datetime(gg['Date'], dayfirst=True)
gg.drop(columns=["ID", "Element"], inplace=True)
gr = gg.groupby(level=0)
m = gr.apply(mn, "Data_Value")
ma = gr.apply(mx, "Data_Value")
gg.drop(columns=["Data_Value"], inplace=True)
gg["min"] = m
gg["max"] = ma
gg.drop_duplicates(inplace=True)
gm = gg.loc["2005":"2014"].groupby([gg.loc["2005":"2014"].index.month, gg.loc["2005":"2014"].index.day])
gk = gm.apply(av, "min")
gl = gm.apply(av, "max")
ng = pd.DataFrame({"min": gk, "max": gl})
ng.drop((2, 29), axis=0, inplace=True)
g2015 = gg.loc["2015"].groupby([gg.loc["2015"].index.month, gg.loc["2015"].index.day])
df = []
ind = []
for i, j in g2015:
    ind.append(i)
    df.append([j["min"][0], j["max"][0]])
d2 = pd.DataFrame(df, ind, columns=["min", 'max'])
d2mn = d2[(d2['min'] < ng["min"])]["min"]
d2ma = d2[(d2['max'] > ng["max"])]["max"]


def manohman(x):
    ff = list(x.index)
    kk = ["2000-{}-{}".format(i, j) for i, j in ff]
    return pd.to_datetime(kk)


kd = manohman(ng)
d2f = manohman(d2mn)
d2l = manohman(d2ma)
plt.figure()
plt.plot(kd, ng["min"], color="#396AB1")
plt.plot(kd, ng["max"], color="#CC2529")
plt.scatter(d2f, d2mn, s=4, color="#DA7C30")
plt.scatter(d2l, d2ma, s=4, color="#3E9651")
plt.fill_between(kd, ng["min"], ng["max"], alpha=0.6, color="grey")
# TODO Set the locator
locator = mdates.MonthLocator()  # every month
# Specify the format - %b gives us Jan, Feb...
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
plt.ylabel("Temp. in °C")
plt.legend(["Low Temp. 2005-2014", "High Temp. 2005-2014", "Temps lower than Previous low on 2015", "Temps "
                                                                                                    "higher "
                                                                                                    "than "
                                                                                                    "previous high on "
                                                                                                    "2015"])
plt.title('Average Daily High and low Temp in Ann Arbor area from 2005-2014\n with outliers 2015 Temps')
plt.show()
