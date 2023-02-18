import pandas as pd
import numpy as np
import re


def a():
    energy = pd.read_excel("Energy+Indicators.xls")
    energy = energy.iloc[17:243]
    energy.reset_index(inplace=True)
    energy.drop(["Unnamed: 0", "Unnamed: 1", "index"], axis=1, inplace=True)
    energy.rename(columns={"Unnamed: 2": 'Country', "Unnamed: 3": 'Energy Supply',
                           "Unnamed: 4": 'Energy Supply per Capita', "Unnamed: 5": '% Renewable'},
                  inplace=True)
    energy["Energy Supply"] = energy["Energy Supply"] * 1000000
    energy["Energy Supply"][~energy["Energy Supply"].astype("str").str.isdigit()] = np.NaN
    energy["Energy Supply per Capita"][~energy["Energy Supply per Capita"].astype("str").str.isdigit()] = np.NaN
    p0 = "[0-9]"
    p1 = "\("
    renameC = {"Republic of Korea": "South Korea",
               "United States of America": "United States",
               "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
               "China, Hong Kong Special Administrative Region": "Hong Kong",
               "Korea, Rep.": "South Korea",
               "Iran, Islamic Rep.": "Iran",
               "Hong Kong SAR, China": "Hong Kong"}
    for i in energy.index:
        if re.search(p1, energy.loc[i, "Country"]):
            energy.loc[i, "Country"] = (
                energy.loc[i, "Country"][:re.search(p1, energy.loc[i, "Country"]).span()[0] - 1])
        if re.search(p0, energy.loc[i, "Country"]):
            energy.loc[i, "Country"] = (energy.loc[i, "Country"][:re.search(p0, energy.loc[i, "Country"]).span()[0]])
        if energy.loc[i, "Country"] in renameC.keys():
            energy.loc[i, "Country"] = renameC[energy.loc[i, "Country"]]
    energy.set_index("Country", inplace=True)
    GDP = pd.read_csv("world_bank.csv")
    GDP = GDP[3:]
    GDP.columns = GDP.iloc[0]
    GDP.columns = GDP.columns.map(str)
    for i in GDP.index:
        if GDP.loc[i, "Country Name"] in renameC.keys():
            GDP.loc[i, "Country Name"] = renameC[GDP.loc[i, "Country Name"]]
    GDP = GDP[1:]
    GDP.reset_index(inplace=True)
    GDP = GDP.loc[:, ["Country Name", 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]]
    GDP.set_index("Country Name", inplace=True)
    ScimEn = pd.read_excel("scimagojr-3.xlsx")
    ScimEn = ScimEn[:15]
    ScimEn.set_index("Country", inplace=True)
    m0 = pd.merge(ScimEn, energy, how="inner", left_index=True, right_index=True)
    m1 = pd.merge(m0, GDP, how="inner", left_index=True, right_index=True)
    return m1


Top15 = a()
Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
t = Top15.loc[:, ['Energy Supply per Capita', 'Citable docs per Capita']]
t.astype("float")
z = t.corr(method='pearson')
print(z)
pd.DataFrame()








