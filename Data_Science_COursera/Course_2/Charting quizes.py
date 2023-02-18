import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mtp

f = plt.figure()

languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
pos = np.arange(len(languages))
popularity = [56, 39, 34, 34, 29]

bar = plt.bar(pos, popularity, align='center', color=["orange", 'grey', 'grey', 'grey', 'grey'], data=popularity)
plt.xticks(pos, languages, color="grey")
plt.title('Top 5 Languages for Math & Data \nby % popularity on Stack Overflow', alpha=0.8)
plt.gca().axes.set_yticks([])
plt.tick_params(axis="x", bottom=False, top=False)
plt.box(False)
for i, v in enumerate(popularity):
    plt.text(i, v - 5, str(v) + "%", fontsize=12, ha="center", color='w', )
plt.show()
