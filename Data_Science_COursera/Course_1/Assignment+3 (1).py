def answer_one():
    import pandas as pd
    import numpy as np
    import re
    energy = pd.read_excel("Energy Indicators.xls")
    energy = energy.iloc[17:243]
    energy.reset_index(inplace=True)
    energy.drop(["Unnamed: 0", "Unnamed: 1", "index"], axis=1, inplace=True)
    energy.rename(columns={"Environmental Indicators: Energy": 'Country', "Unnamed: 3": 'Energy Supply',
                           "Unnamed: 4": 'Energy Supply per Capita', "Unnamed: 5": '% Renewable'},
                  inplace=True)
    se = energy.shape
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
    GDP.columns = list(GDP.iloc[0][:5]) + list(GDP.iloc[0][5:].map(int).map(str))
    sg = GDP.shape
    for i in GDP.index:
        if GDP.loc[i, "Country Name"] in renameC.keys():
            GDP.loc[i, "Country Name"] = renameC[GDP.loc[i, "Country Name"]]
    GDP = GDP[1:]
    GDP.reset_index(inplace=True)
    GDP = GDP.loc[:, ["Country Name", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]]
    GDP.set_index("Country Name", inplace=True)
    ScimEn = pd.read_excel("scimagojr-3.xlsx")
    ss = ScimEn.shape
    ScimEn.set_index("Country", inplace=True)
    m0 = pd.merge(ScimEn, energy, how="inner", left_index=True, right_index=True)
    m1 = pd.merge(m0, GDP, how="inner", left_index=True, right_index=True)
    m1.sort_values(by="Rank", ascending=True, inplace=True)
    return m1[:15]


# ### Question 2 (6.6%) The previous question joined three datasets then reduced this to just the top 15 entries.
# When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

def answer_two():
    return 18332 - (15 * 20)


# ## Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*


def answer_three():
    import numpy as np
    Top15 = answer_one()
    for i in Top15.index:
        Top15.loc[i, "avgGDP"] = np.average(Top15.loc[
                                                i, ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
                                                    "2014", "2015"]].dropna().unique())
    return Top15['avgGDP']


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*
# 

# In[58]:


def answer_four():
    import numpy as np
    Top15 = answer_one()
    av = answer_three()
    av = av.sort_values(ascending=False).copy().index[5]
    return abs(Top15.loc[av, "2006"] - Top15.loc[av, "2015"])


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[59]:


def answer_five():
    Top15 = answer_one()
    import numpy as np
    m = np.nanmean(Top15["Energy Supply per Capita"])
    return m


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[68]:


def answer_six():
    Top15 = answer_one()
    ct = Top15.copy()
    ct.sort_values(by="% Renewable", inplace=True, ascending=False)
    return (ct.index[0], ct.iloc[0]["% Renewable"])


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[20]:


def answer_seven():
    Top15 = answer_one()
    t = Top15.copy()
    t["ratio"] = t['Self-citations'] / t["Citations"]
    return (t[t["ratio"] == max(t["ratio"])].index[0], t.loc[t[t["ratio"] == max(t["ratio"])].index[0]]['ratio'])


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[31]:


def answer_eight():
    Top15 = answer_one()
    t = Top15.copy()
    t["POPESTIMATE"] = t["Energy Supply"] / t["Energy Supply per Capita"]
    t.sort_values(by="POPESTIMATE", inplace=True, ascending=False)
    return t.iloc[2].name


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's1 correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[46]:


def answer_nine():
    Top15 = answer_one()
    import numpy as np
    Top15['PopEst'] = np.float64(Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    Top15['Citable docs per Capita'] = np.float64(Top15['Citable documents'] / Top15['PopEst'])
    Top15["Energy Supply per Capita"] = np.float64(Top15["Energy Supply per Capita"])
    return Top15["Energy Supply per Capita"].corr(Top15['Citable docs per Capita'], method='pearson')


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's1 % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's1 % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[80]:


def answer_ten():
    Top15 = answer_one()
    import numpy as np
    m = np.median(Top15["% Renewable"])
    for i in Top15.index:
        if Top15.loc[i, "% Renewable"] >= m:
            Top15.loc[i, 'HighRenew'] = 1
        else:
            Top15.loc[i, "HighRenew"] = 0

    Top15["HighRenew"] = Top15["HighRenew"].astype(int)
    return Top15["HighRenew"]


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[78]:


def answer_eleven():
    import pandas as pd
    import numpy as np
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15 = answer_one()
    Top15['PopEst'] = np.float64(Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    c = pd.Series(ContinentDict)
    Top15["c"] = c
    T = Top15.groupby("c")["PopEst"]
    size = T.apply(len, ).astype("float")
    su = T.apply(sum)
    mean = T.apply(np.mean)
    std = T.apply(np.std)
    df = pd.DataFrame({"mean": mean, 'sum': su, "size": size, "std": std})
    df.index.name = None
    df = df[['size', 'sum', 'mean', 'std']]
    return df


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[105]:


def answer_twelve():
    Top15 = answer_one()
    import pandas as pd
    s = pd.cut(Top15["% Renewable"], 5)
    import numpy as np
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15 = answer_one()
    Top15['PopEst'] = np.float64(Top15['Energy Supply'] / Top15['Energy Supply per Capita'])
    c = pd.Series(ContinentDict)
    Top15["Continent"] = c
    T = Top15.groupby(("Continent", s)).apply(len)
    return T


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[31]:


def answer_thirteen():
    Top15 = answer_one()
    import numpy as np
    import re
    Top15['PopEst'] = np.float64(Top15['Energy Supply'] / Top15['Energy Supply per Capita']).astype("str")

    def fu(x):
        p = r"\."
        z = list(x)
        g = re.search(p, x).span()[0]
        for i in range(g, 0, -3):
            if i == g:
                continue
            z.insert(i, ",")
        return "".join(z)

    return Top15["PopEst"].apply(fu)


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[71]:
